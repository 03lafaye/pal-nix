#!/usr/bin/python

"""
    Module for looking up symbolic debugging information.
    The information can include symbol names, offsets, and source locations.
    Make sure you've called envsetup.sh to setup your environment variables for Chrome
"""

import os
import re
import subprocess
import sys

if not os.environ.has_key('CHROME_SRC'):
    sys.exit('CHROME_SRC is not defined. Make sure you have run build/android/envsetup.sh')

SYMBOLS_DIR = '%s/out/Debug/lib.target' % os.environ['CHROME_SRC']
TOOLCHAIN_BIN = os.environ['ANDROID_TOOLCHAIN']

def ToolPath(tool):
    return '%s/arm-linux-androideabi-%s' % (TOOLCHAIN_BIN, tool)

def SymbolInformation(lib, addr):
  """Look up symbol information about an address.

  Args:
    lib: library (or executable) pathname containing symbols
    addr: string hexidecimal address

  Returns:
    For a given library and address, return tuple of: (source_symbol,
    source_location, object_symbol_with_offset) the values may be None
    if the information was unavailable.

    source_symbol may not be a prefix of object_symbol_with_offset if
    the source function was inlined in the object code of another
    function.

    usually you want to display the object_symbol_with_offset and
    source_location, the source_symbol is only useful to show if the
    address was from an inlined function.
  """
  info = SymbolInformationForSet(lib, set([addr]))
  return (info and info.get(addr)) or (None, None, None)


def SymbolInformationForSet(lib, unique_addrs):
  """Look up symbol information for a set of addresses from the given library.

  Args:
    lib: library (or executable) pathname containing symbols
    unique_addrs: set of hexidecimal addresses

  Returns:
    For a given library and set of addresses, returns a dictionary of the form
    {addr: (source_symbol, source_location, object_symbol_with_offset)}. The
    values may be None if the information was unavailable.

    For a given address, source_symbol may not be a prefix of
    object_symbol_with_offset if the source function was inlined in the
    object code of another function.

    Usually you want to display the object_symbol_with_offset and
    source_location; the source_symbol is only useful to show if the
    address was from an inlined function.
  """
  if not lib:
    return None

  addr_to_line = CallAddr2LineForSet(lib, unique_addrs)
  if not addr_to_line:
    return None

  addr_to_objdump = CallObjdumpForSet(lib, unique_addrs)
  if not addr_to_objdump:
    return None

  result = {}
  for addr in unique_addrs:
    (source_symbol, source_location) = addr_to_line.get(addr, (None, None))
    if addr in addr_to_objdump:
      (object_symbol, object_offset) = addr_to_objdump.get(addr)
      object_symbol_with_offset = FormatSymbolWithOffset(object_symbol,
                                                         object_offset)
    else:
      object_symbol_with_offset = None
    result[addr] = (source_symbol, source_location, object_symbol_with_offset)

  return result


def CallAddr2LineForSet(lib, unique_addrs):
  """Look up line and symbol information for a set of addresses.

  Args:
    lib: library (or executable) pathname containing symbols
    unique_addrs: set of string hexidecimal addresses look up.

  Returns:
    A dictionary of the form {addr: (symbol, file:line)}. The values may
    be (None, None) if the address could not be looked up.
  """
  if not lib:
    return None


  symbols = '%s/%s' % (SYMBOLS_DIR, lib)
  if not os.path.exists(symbols):
    return None

  cmd = [ToolPath("addr2line"), "--functions", "--demangle", "--exe=" + symbols]
  child = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

  result = {}
  addrs = sorted(unique_addrs)
  for addr in addrs:
    child.stdin.write("0x%s\n" % addr)
    child.stdin.flush()
    symbol = child.stdout.readline().strip()
    if symbol == "??":
      symbol = None
    location = child.stdout.readline().strip()
    if location == "??:0":
      location = None
    result[addr] = (symbol, location)
  child.stdin.close()
  child.stdout.close()
  return result


def CallObjdumpForSet(lib, unique_addrs):
  """Use objdump to find out the names of the containing functions.

  Args:
    lib: library (or executable) pathname containing symbols
    unique_addrs: set of string hexidecimal addresses to find the functions for.

  Returns:
    A dictionary of the form {addr: (string symbol, offset)}.
  """
  if not lib:
    return None

  symbols = '%s/%s' % (SYMBOLS_DIR, lib)
  if not os.path.exists(symbols):
    return None 

  addrs = sorted(unique_addrs)
  start_addr_hex = addrs[0]
  stop_addr_dec = str(int(addrs[-1], 16) + 8)
  cmd = [ToolPath("objdump"),
         "--section=.text",
         "--demangle",
         "--disassemble",
         "--start-address=0x" + start_addr_hex,
         "--stop-address=" + stop_addr_dec,
         symbols]

  # Function lines look like:
  #   000177b0 <android::IBinder::~IBinder()+0x2c>:
  # We pull out the address and function first. Then we check for an optional
  # offset. This is tricky due to functions that look like "operator+(..)+0x2c"
  func_regexp = re.compile("(^[a-f0-9]*) \<(.*)\>:$")
  offset_regexp = re.compile("(.*)\+0x([a-f0-9]*)")

  # A disassembly line looks like:
  #   177b2:	b510      	push	{r4, lr}
  asm_regexp = re.compile("(^[ a-f0-9]*):[ a-f0-0]*.*$")

  current_symbol = None    # The current function symbol in the disassembly.
  current_symbol_addr = 0  # The address of the current function.
  addr_index = 0  # The address that we are currently looking for.

  stream = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout
  result = {}
  for line in stream:
    # Is it a function line like:
    #   000177b0 <android::IBinder::~IBinder()>:
    components = func_regexp.match(line)
    if components:
      # This is a new function, so record the current function and its address.
      current_symbol_addr = int(components.group(1), 16)
      current_symbol = components.group(2)

      # Does it have an optional offset like: "foo(..)+0x2c"?
      components = offset_regexp.match(current_symbol)
      if components:
        current_symbol = components.group(1)
        offset = components.group(2)
        if offset:
          current_symbol_addr -= int(offset, 16)

    # Is it an disassembly line like:
    #   177b2:	b510      	push	{r4, lr}
    components = asm_regexp.match(line)
    if components:
      addr = components.group(1)
      target_addr = addrs[addr_index]
      i_addr = int(addr, 16)
      i_target = int(target_addr, 16)
      if i_addr == i_target:
        result[target_addr] = (current_symbol, i_target - current_symbol_addr)
        addr_index += 1
        if addr_index >= len(addrs):
          break
  stream.close()

  return result


def CallCppFilt(mangled_symbol):
  cmd = [ToolPath("c++filt")]
  process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  process.stdin.write(mangled_symbol)
  process.stdin.write("\n")
  process.stdin.close()
  demangled_symbol = process.stdout.readline().strip()
  process.stdout.close()
  return demangled_symbol

def FormatSymbolWithOffset(symbol, offset):
  if offset == 0:
    return symbol
  return "%s+%d" % (symbol, offset)

#! /usr/bin/env python

"""
This script will convert a color representation from RGB to Hex or Hex to RGB
depending on the input.

Usage:
  $ rgbhex.py ffffff
  (255, 255, 255)

  $rgbhex.py 255,255,255
  #fffff

"""

import sys, pdb

def rgb_to_html_color(rgb_tuple):
    """ convert an (R, G, B) tuple to #RRGGBB """
    hexcolor = '#%02x%02x%02x' % rgb_tuple
    # that's it! '%02x' means zero-padded, 2-digit hex values
    return hexcolor

def html_color_to_rgb(colorstring):
    """ convert #RRGGBB to an (R, G, B) tuple """
    colorstring = colorstring.strip()
    if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

def convert_color(color_str):
  if color_str[0] == '#' or color_str[0] > '9':
    return html_color_to_rgb(color_str)
  rgb = color_str.split(',')
  if (len(rgb) == 3): 
    rgb_tuple = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
    return rgb_to_html_color(rgb_tuple)

  raise('Invalid color input: %s' % color_str)

def main():
  for arg in sys.argv[1:]:
    print(convert_color(arg))

if __name__ == '__main__':
  main()

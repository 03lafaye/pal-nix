#!/usr/bin/env python

from Crypto.Cipher import AES
import base64
import os
import sys

# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

SECRET_FILE = 'secret.txt'
PWD_FILE = 'site-passwd.txt'

def encode_sites():
    """ Takes in comma separated name,passwd pairs from stdin and writes
    name,encoded pairs to PWD_FILE. """
    # generate a random secret key
    secret = os.urandom(BLOCK_SIZE)
    open(SECRET_FILE, 'w').write(secret)

    # create a cipher object using the random secret
    cipher = AES.new(secret)

    site_file = open(PWD_FILE, 'w')

    for line in sys.stdin:
        site, pwd = line.strip().split(',')
        encoded = EncodeAES(cipher, pwd)
        site_file.write("%s,%s\n" % (site, encoded))

    site_file.close()
    return 0

def decode_sites():
    """ Reads in comma separated name,encoded pairs and attempts to decode the
    encoded pwd using the secret in SECRET_FILE. """
    secret_file = open(SECRET_FILE)
    secret = AES.new(secret_file.read())
    secret_file.close()
    for line in sys.stdin:
        site, encoded = line.strip().split(',')
        # decode the encoded string
        decoded = DecodeAES(secret, encoded)
        print('%s,%s' % (site, decoded))
    return 0

USAGE = "cat pwd_file | pycrypto.py -e\ncat encoded | pycrypto.py -d"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(USAGE)
    if sys.argv[1] == '-e':
        sys.exit(encode_sites())
    elif sys.argv[1] == '-d':
        sys.exit(decode_sites())
    sys.exit(USAGE)

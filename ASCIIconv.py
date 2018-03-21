#!/usr/bin/env python
# Convert to and from ASCII and Hex
# source: https://github.com/carmeloc/ASCIIconv
# history, date format ISO 8601:
#  2018-03-21 1.0 initial version

from __future__ import print_function	# future statement definitions
import argparse				# write user-friendly command-line interfaces
import sys				# system-specific parameters and functions

# Version number
__version__ = 1.0
__build__ = 180321

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    if args.filename:
        string = open(args.filename).read()
        conv(string.rstrip())
    elif not sys.stdin.isatty():
        string = sys.stdin.read()
        conv(string.rstrip())
    else:
        parser.print_help()

def conv(s):
    l = [hex(ord(i)) for i in s]
    print(l)
#    for i in s:
#        sys.stdout.write(hex(ord(i)))

#    for line in sys.stdin:
#        sys.stderr.write("DEBUG: got line: " + line)
#        sys.stdout.write(line)

if __name__ == "__main__":
    main()

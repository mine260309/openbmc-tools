#!/usr/bin/env python

import os
import sys

def main():

    if len(sys.argv) != 3:
        print "Usage: sbefifo.py <device> <message>"
        exit(1)

    # This is only a script for testing purpose
    # example device = "/dev/sbefifo1"
    # example hex_string = "000000030000a7010001fff1"

    device = sys.argv[1]
    hex_string = sys.argv[2]
    hex_bytes = hex_string.decode("hex")
    print str(hex_bytes.encode("hex"))

    dev = os.open(device, os.O_RDWR)
    os.write(dev, hex_bytes)

    response = os.read(dev, 16)
    print str(response.encode("hex"))

if __name__ == "__main__":
    main()

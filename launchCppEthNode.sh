#!/usr/bin/env bash
set -v  # Verbose on: echo all lines in this script

#
# Full Node
#

#eth -j -b -n off -m on


#
# Peer Node (aka "bootstrap" node)
#

# Run ifconfig to get the correct IP address.
#eth -m off -o peer -u 192.168.0.5 -p 30333 -n off
eth -m off -o peer -u 192.168.0.5 -p 30333 -x 256

#!/usr/bin/env bash
set -v  # Verbose on: echo all lines in this script

#
# Full Node
#

# ? I'm not sure if these are really full nodes?
#pyeth -r 127.0.0.1 -p 30300 -l 30301 -d /tmp/data1/
#pyeth -r 127.0.0.1 -p 30300 -l 30302 -d /tmp/data2/
#pyeth -r 127.0.0.1 -p 30300 -l 30303 -d /tmp/data3/


#
# Peer Node (aka "bootstrap" node)
#

pyeth -l 30300 -d /tmp/data0/


#!/usr/bin/env bash
set -v  # Verbose on: echo all lines in this script

# WARNING: The Go node is *extremely* sluggish and may freeze up machine.

# If things don't work, then delete old block chain:
# rm -rf ~/.ethereum || rm -rf ~/.ethereal


#
# Full Node
#

# To get the node's address, run: ethereum address
#ethereum --mine --rpc --rpcport "8080" --unlock=ethereum_address_here:password


#
# Peer Node (aka "bootstrap" node)
#

echo At the prompt, type: eth.addPeer('107.178.217.2:30303')
ethereum -seed=false -js=true


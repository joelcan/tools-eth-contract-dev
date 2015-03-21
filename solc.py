#!/usr/bin/env python

"""
solc = Solidity compiler
You must install the solc binary first.
"""

from __future__ import print_function #This *must* be the first line
import sys
import os
import subprocess


# Contracts & related files
mul7 = 'mul7.sol'
abi_filename = 'test.abi'
evm_filename = 'test.binary'

def rm_temp_files():
    try:
        os.remove(abi_filename)
    except OSError:
        pass
    try:
        os.remove(evm_filename)
    except OSError:
        pass

def solc(src):
    # TODO: Change from 'file' to 'stdout' and call separately
    exit_code = subprocess.call(
            ['solc'
                ,'--input-file', src
                ,'--binary', 'file'
                ,'--json-abi', 'file'
                ]
            )
    if exit_code:
        raise Exception('solc returned error code: {}'.format(exit_code))
    abi_file = open(abi_filename)
    evm_file = open(evm_filename)
    rm_temp_files()
    return abi_file.read(), evm_file.read()

# TODO: Add command line usage explanation
def main():
    """Handle command line parameters"""
    i = 1
    while i < len(sys.argv):
        parm = sys.argv[i]
        abi, evm = solc(parm)
        print('')
        print('===')
        print(parm)
        print('===')
        print(abi)
        print(evm)
        print('===')
        i = i+1

if __name__ == "__main__":
    main()


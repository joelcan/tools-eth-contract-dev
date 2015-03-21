#!/usr/bin/env python

from __future__ import print_function  # This *must* be the first line
import sys
import os
import subprocess
from pyethereum import tester, utils, transactions, blocks, processblock, rlp
import serpent
from solc import solc


# TODO: Figure out why state cannot be created as an attribute.
state = tester.state()  # Create test blockchain

class Mul7():

    OWNER = {'address': tester.a0, 'key': tester.k0}
    MANAGER1 = {'address': tester.a1, 'key': tester.k1}
    USER1 = {'address': tester.a2, 'key': tester.k2}

    mul7 = 'mul7.sol'
    mul7se = 'mul7.se'

    # Setup
    def Mul7(self):
        #self.state = tester.state()  # Create test blockchain
        pass

    def loadContract(self, src_filename):
        # Serpent version
        mul7se_src = open(self.mul7se).read()
        print('>>> Serpent src: {}'.format(mul7se_src))
        self.mul7se_addr = state.contract(
                mul7se_src, 
                self.OWNER['key'], 
                0)
        #self.mul7se_evm = self.state.abi_contract(self.mul7se)
        #self.mul7se_evm = serpent.compile(open(self.mul7se).read())
        #self.mul7se_rlp_decode = rlp.decode(self.mul7se_evm)
        #print('>>> Serpent compile: {}'.format(self.mul7se_evm))
        #print('>>> Serpent rlp-decode: {}'.format(self.mul7se_rlp_decode))
        #self.state.evm(self.mul7_evm, sender=self.OWNER, endowment=0)

        # Solidity version
        _, self.mul7_evm = solc(src_filename)  # Compile
        #self.mul7_evm = '0x{}'.format(self.mul7_evm)
        print('>>> Solidity evm: {}'.format(self.mul7_evm))
        self.mul7_addr = state.contract_from_evm(
                self.mul7_evm, 
                self.OWNER['key'], 
                0)
        print('>>> Solidity contract address: {}'.format(self.mul7_addr))
        #self.state.evm(self.mul7_evm, sender=self.OWNER[], endowment=0)

        #self.state.mine(n=1, coinbase=self.OWNER)
        #self.snapshot = self.state.snapshot()


# TODO: Add command line usage explanation
def main():
    """Handle command line parameters"""
    if len(sys.argv) == 1:
        print('Usage:')
        print('  {} <solidity-source-code-filename>'.format(sys.argv[0]))
        c.loadContract(c.mul7)
    else:
        c = Mul7()
        i = 1
        while i < len(sys.argv):
            parm = sys.argv[i]
            c.loadContract(parm)
            i = i+1


if __name__ == "__main__":
    main()


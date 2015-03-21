from __future__ import print_function  # This *must* be the first line
import pytest
import os
import subprocess
from pyethereum import tester, utils, transactions, blocks, processblock, rlp
import serpent
from solc import solc


class TestMul7(object):

    OWNER = {'address': tester.a0, 'key': tester.k0}
    MANAGER1 = {'address': tester.a1, 'key': tester.k1}
    USER1 = {'address': tester.a2, 'key': tester.k2}

    # Contracts
    mul7 = 'mul7.sol'
    mul7se = 'mul7.se'

    # Setup
    def setup_class(self):
        self.state = tester.state()  # Create test blockchain

        # Solidity version
        _, self.mul7_evm = solc(self.mul7)  # Compile
        print('>>> Solidity evm: {}'.format(self.mul7_evm))
        self.addr = self.state.contract(self.mul7_evm, OWNER['key'], 0)
        print('>>> Solidity contract address: {}'.format(self.addr))
        #self.mul7_evm = '0x{}'.format(self.mul7_evm)
        self.mul7_decoded = self.mul7_evm.decode('hex')
        print('>>> Solidity decode-hex: {}'.format(self.mul7_evm.decode('hex')))
        #self.state.evm(self.mul7_evm, sender=self.OWNER, endowment=0)
        self.state.evm(self.mul7_decoded, sender=self.OWNER, endowment=0)

        # Serpent version
        #self.mul7se_evm = self.state.abi_contract(self.mul7se)
        self.mul7se_evm = serpent.compile(open(self.mul7se).read())
        self.mul7se_rlp_decode = rlp.decode(self.mul7se_evm)
        print('>>> Serpent compile: {}'.format(self.mul7se_evm))
        #print('>>> Serpent rlp-decode: {}'.format(self.mul7se_rlp_decode))
        #self.state.evm(self.mul7_evm, sender=self.OWNER, endowment=0)

        #self.state.mine(n=1, coinbase=self.OWNER)
        #self.snapshot = self.state.snapshot()


    def setup_method(self, method):
        #self.state.revert(self.snapshot)
        pass


    # Tests
    def test_mul7(self):
        #ans = self.mul7.register(self.OWNER['address'])
        assert False


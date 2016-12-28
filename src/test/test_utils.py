__author__ = 'erasmospunk'

import unittest
from utils import hash_160_to_address, bc_address_to_hash_160


class UtilTest(unittest.TestCase):

    def test_hash_160_to_address(self):
        self.assertEqual(hash_160_to_address(None), None)
        self.assertEqual(hash_160_to_address('04e9fca1'.decode('hex')), None)
        self.assertEqual(hash_160_to_address('04e9fca1f96e021dfaf35bbea267ec2c60787c1b1337'.decode('hex')), None)
        self.assertEqual(hash_160_to_address('ce2a79d5c9d8ba7096d218fb82aa16f01e6dff48'.decode('hex')),'Sg677dvc44YEV8u5nTo1STR7P51ikfBDzm')


    def test_bc_address_to_hash_160(self):
        self.assertEqual(bc_address_to_hash_160(None), None)
        self.assertEqual(bc_address_to_hash_160(''), None)
        self.assertEqual(bc_address_to_hash_160('Sg677dvc44YEV8u5nTo1STR7P51ikfBDzm1337'), None)
        self.assertEqual(bc_address_to_hash_160('Sg677dvc44YEV8u5nTo1STR7P51ikfBDzm').encode('hex'),'ce2a79d5c9d8ba7096d218fb82aa16f01e6dff48')



if __name__ == '__main__':
    unittest.main()


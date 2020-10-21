import unittest
from unittest import mock
import sys,os

sys.path.append(os.path.dirname(os.getcwd()))
from solution.sln import validate_email_addr

class TestEmail(unittest.TestCase):

    def test_email(self):
        with mock.patch('builtins.input',
        side_effect = ["DEXTER <dexter@hotmail.com>","VIRUS <virus!@variable.:p>"]):
            self.assertEqual(validate_email_addr(2),"DEXTER <dexter@hotmail.com>","Invalid Email")
            
if __name__ == "__main__":
    unittest.main()

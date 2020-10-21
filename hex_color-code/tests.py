import unittest
from unittest import mock
from sln import get_hex_code

class TestHexcode(unittest.TestCase):

    def test_csscode(self):
        with mock.patch('builtins.input',
        side_effect=["#BED",
        "{",
        "color: #FfFdF8; background-color:#aef;",
        "font-size: 123px;",
        "background: -webkit-linear-gradient(top, #f9f9f9, #fff);",
        "}",
        "#Cab",
        "{","background-color: #ABC;",
        "border: 2px dashed #fff;",
        "}"]):
            self.assertEqual(get_hex_code(11),
            ["#FfFdF8","#aef","#f9f9f9","#fff","#ABC","#fff"],"Invalid Hex Code")
            
if __name__ == "__main__":
    unittest.main()

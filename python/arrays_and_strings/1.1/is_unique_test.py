import unittest

from is_unique import is_unique

class UniqueTests(unittest.TestCase):

    def test_is_unique_loan(self):
        self.assertEqual(True, is_unique("loan"))

    def test_is_unique_false(self):
        self.assertEqual(False, is_unique("lol"))

    def test_is_unique_alphabet(self):
        self.assertEqual(True, is_unique("abcdefghijklmnopqrstuvwxyz"))
        
    def test_is_unique_alphabet_plus_1(self):
        self.assertEqual(False, is_unique("abcdefghijklmnoprstuvwqxyzj"))

    def test_is_unique_empty(self):
        self.assertEqual(False, is_unique(""))

if __name__ == '__main__':
    unittest.main()

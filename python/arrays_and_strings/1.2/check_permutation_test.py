import unittest

from check_permutation import check_permutation

class CheckPermutationTest(unittest.TestCase):

    def test_is_permutation(self):
        self.assertEqual(True, check_permutation("is", "si"))

    def test_is_permutation_longer(self):
        self.assertEqual(True, check_permutation("aaabbbccc", "abcabcabc"))

    def test_is_not_permutation(self):
        self.assertEqual(False, check_permutation("lol", "lol2"))

    def test_is_not_permutation_longer(self):
        self.assertEqual(False, check_permutation("lololol", "looool"))

if __name__ == '__main__':
    unittest.main()

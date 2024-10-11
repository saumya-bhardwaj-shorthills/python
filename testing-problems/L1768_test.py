import unittest
from L1768 import mergeAlternately 

class TestMergeAlternately(unittest.TestCase):

    def test_example1(self):
        word1 = "abc"
        word2 = "pqr"
        expected_output = "apbqcr"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_example2(self):
        word1 = "ab"
        word2 = "pqrs"
        expected_output = "apbqrs"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_example3(self):
        word1 = "abcd"
        word2 = "pq"
        expected_output = "apbqcd"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_empty_string1(self):
        word1 = ""
        word2 = "xyz"
        expected_output = "xyz"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_empty_string2(self):
        word1 = "abc"
        word2 = ""
        expected_output = "abc"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_both_empty(self):
        word1 = ""
        word2 = ""
        expected_output = ""
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_same_length(self):
        word1 = "abcde"
        word2 = "vwxyz"
        expected_output = "avbwcxdyez"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_different_lengths1(self):
        word1 = "abc"
        word2 = "defgh"
        expected_output = "adbecfgh"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

    def test_different_lengths2(self):
        word1 = "wxyz"
        word2 = "st"
        expected_output = "wsxtyz"
        self.assertEqual(mergeAlternately(word1, word2), expected_output)

if __name__ == "__main.py__":
    unittest.main()

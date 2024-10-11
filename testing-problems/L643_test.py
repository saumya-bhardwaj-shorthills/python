import unittest
from L643 import canPlaceFlowers 

class TestCanPlaceFlowers(unittest.TestCase):

    def test_example1(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 1
        expected_output = True
        self.assertEqual(canPlaceFlowers(flowerbed, n), expected_output)

    def test_example2(self):
        flowerbed = [1, 0, 0, 0, 1]
        n = 2
        expected_output = False
        self.assertEqual(canPlaceFlowers(flowerbed, n), expected_output)

    def test_no_flowers_needed(self):
        flowerbed = [0, 0, 0, 0, 0]
        n = 0
        expected_output = True
        self.assertEqual(canPlaceFlowers(flowerbed, n), expected_output)

    def test_single_empty_plot(self):
        flowerbed = [0]
        n = 1
        expected_output = True
        self.assertEqual(canPlaceFlowers(flowerbed, n), expected_output)

    def test_single_full_plot(self):
        flowerbed = [1]
        n = 1
        expected_output = False
        self.assertEqual(canPlaceFlowers(flowerbed, n), expected_output)

    def test_all_zeros(self):
        flowerbed = [0, 0, 0, 0, 0, 0, 0]
        n = 3
        expected_output = True
        self.assertEqual(canPlaceFlowers(flowerbed, n), expected_output)

    def test_all_ones(self):
        flowerbed = [1, 1, 1, 1, 1]
        n = 1
        expected_output = False
        self.assertEqual(canPlaceFlowers(flowerbed, n), expected_output)

if __name__ == "__main__":
    unittest.main()

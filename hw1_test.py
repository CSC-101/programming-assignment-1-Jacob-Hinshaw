import data
import hw1
import unittest


#def test_first_element_1(self):
#    input = [[1, 2], [3, 4]]
#    result = lab4.first_element(input)
#    expected = [1, 3]
#    self.assertEqual(expected, result)

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test1_vowel_count(self):
        input = "Hey ThEre"
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected, result)
    def test21_vowel_count(self):
        input = "Vowels Are Cool"
        result = hw1.vowel_count(input)
        expected = 6
        self.assertEqual(expected, result)

    # Part 2



    # Part 3


    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()

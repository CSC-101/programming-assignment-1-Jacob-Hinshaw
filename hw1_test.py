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
    def test2_vowel_count(self):
        input = "Vowels Are Cool"
        result = hw1.vowel_count(input)
        expected = 6
        self.assertEqual(expected, result)

    # Part 2
    def test1_short_lists(self):
        input = [[1], [2,3], [4,5,6], [7,8,9], [10,11], [12]]
        result = hw1.short_lists(input)
        expected = [[2,3], [10,11]]
        self.assertEqual(expected, result)
    def test1_short_lists(self):
        input = [[10], [9,8,7,6,5,4], [3,2], [1]]
        result = hw1.short_lists(input)
        expected = [[3,2]]
        self.assertEqual(expected, result)

    # Part 3
    def test1_ascending_pairs(self):
        input = [[1], [3,2], [4,5,6], [7,8], [9]]
        result = hw1.ascending_pairs(input)
        expected = [[1], [2,3], [4,5,6], [7,8], [9]]
        self.assertEqual(expected, result)
    def test2_ascending_pairs(self):
        input = [[9], [1,1], [3,1,6], [8,7], [12]]
        result = hw1.ascending_pairs(input)
        expected = [[9], [1,1], [3,1,6], [7,8], [12]]
        self.assertEqual(expected, result)

    # Part 4
    def test1_add_prices(self):
        input1 = data.Price(2,60)
        input2 = data.Price(3, 75)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(6, 35)
        self.assertEqual(expected, result)
    def test2_add_prices(self):
        input1 = data.Price(1,30)
        input2 = data.Price(2, 20)
        result = hw1.add_prices(input1, input2)
        expected = data.Price(3, 50)
        self.assertEqual(expected, result)

    # Part 5
    def test1_rectangle_area(self):
        input1 = data.Rectangle(data.Point(0,0), data.Point(2,2))
        result = hw1.rectangle_area(input1)
        expected = 4
        self.assertEqual(expected, result)
    def test2_rectangle_area(self):
        input1 = data.Rectangle(data.Point(-5,-5), data.Point(2,2))
        result = hw1.rectangle_area(input1)
        expected = 49
        self.assertEqual(expected, result)

    # Part 6


    # Part 7


    # Part 8




if __name__ == '__main__':
    unittest.main()

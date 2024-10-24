import data
import hw1
import unittest

from data import Employee
from hw1 import books_by_author


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
    def test1_books_by_author(self):
        input1 = "Sophia"
        input2 = [data.Book(["Sophia", "Jacob"], "Fish"),
                  data.Book(["Jacob"], "Unicycle"), data.Book(["Sophia"], "Flute")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book(["Sophia", "Jacob"],"Fish"), data.Book(["Sophia"], "Flute")]
        self.assertEqual(expected, result)
    def test2_books_by_author(self):
        input1 = "Jacob"
        input2 = [data.Book(["Sophia", "Jacob"], "Fish"),
                  data.Book(["Jacob"], "Unicycle"), data.Book(["Sophia"], "Flute")]
        result = hw1.books_by_author(input1, input2)
        expected = [data.Book(["Sophia", "Jacob"],"Fish"), data.Book(["Jacob"], "Unicycle")]
        self.assertEqual(expected, result)

    # Part 7
    def test1_circle_bound(self):
        input1 = data.Rectangle(data.Point(0,0),data.Point(4,2))
        result = hw1.circle_bound(input1)
        expected = data.Circle(data.Point(2,1), 5**(1/2))
        self.assertEqual(expected, result)
    def test2_circle_bound(self):
        input1 = data.Rectangle(data.Point(-3,5),data.Point(1,1))
        result = hw1.circle_bound(input1)
        expected = data.Circle(data.Point(-1,3), 8**(1/2))
        self.assertEqual(expected, result)

    # Part 8
    def test1_below_pay_average(self):
        input1 = [Employee("Jacob",20),Employee("Sophia", 30),
                  Employee("Travis", 15), Employee("Dylan", 10)]
        result = hw1.below_pay_average(input1)
        expected = ["Travis", "Dylan"]
        self.assertEqual(expected, result)
    def test2_below_pay_average(self):
        input1 = [Employee("Jacob",10),Employee("Sophia", 10),
                  Employee("Travis", 10)]
        result = hw1.below_pay_average(input1)
        expected = []
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
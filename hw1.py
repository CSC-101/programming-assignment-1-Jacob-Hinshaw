import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(word:str) -> int:    # A string is inputted, the number of vowels are counted,
    count = 0                        # and a float value is outputted
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            count += 1
    return count

# Part 2
def short_lists(long:list[list[int]]) -> list[list[int]]: # This code takes a list of lists of integers and
    result_list = []                                      # returns a list of lists of integers that only have
    for group in long:                                    # 2 integers in them
        if len(group) == 2:
            result_list.append(group)
    return result_list

# Part 3
# This code takes a list of lists of integers and returns a new list of lists of integers which all internal
# lists which only have two numbers will be organized from smallest to largest.
def ascending_pairs(input_list:list[list[int]]) -> list[list[int]]:
    result_list = []
    for sub_list in input_list:
        if len(sub_list) == 2:
            if sub_list[0] <= sub_list[1]:
                result_list.append(sub_list)
            else:
                result_list.append([sub_list[1], sub_list[0]])
        else:
            result_list.append(sub_list)
    return result_list

# Part 4
# This code takes two prices of the Price class and adds them together, then converts cents over 100 to dollars
# and then returns it as a Price class.
def add_prices(price1:data.Price, price2:data.Price) -> data.Price:
    price3 = data.Price(0,0)
    price3.dollars = price1.dollars + price2.dollars
    price3.cents = price1.cents + price2.cents
    while price3.cents > 99:
        price3.dollars += 1
        price3.cents -= 100
    return price3

# Part 5
# This function takes an input of class Rectangle and calculates the rectangles area and returns it as a float.
def rectangle_area(rect:data.Rectangle) -> float:
    x_length = abs(rect.top_left.x - rect.bottom_right.x)
    y_length = abs(rect.top_left.y - rect.bottom_right.y)
    return x_length * y_length

# Part 6
# This function takes an author as a string and a list of class type Books and returns a list of class type
# Books, but only the ones with the inputted author.
def books_by_author(author:str, books:list[data.Book]):
    new_books = []
    for book in books:
        for book_author in book.authors:
            if book_author == author:
                new_books.append(book)
    return new_books

# Part 7
# this function takes a input of class type Rectangle and give the output of class type Circle which is the
# smallest bounding circle for the given rectangle.
def circle_bound(rect:data.Rectangle) -> data.Circle:
    x_center = (rect.top_left.x+rect.bottom_right.x)/2
    y_center = (rect.top_left.y+rect.bottom_right.y)/2
    radius = (((rect.top_left.x-rect.bottom_right.x)/2)**2 + ((rect.top_left.y-rect.bottom_right.y)/2)**2)**(1/2)
    center = data.Point(x_center, y_center)
    return data.Circle(center,radius)

# Part 8
# This function takes a list of class type Employees and calculates the average pay rate, it then returns
# a list of names of any employee who's pay is below average of employees in the original list.
def below_pay_average(all:list[data.Employee]) -> list[str]:
    avg_pay_rate = sum(employee.pay_rate for employee in all) / len(all)
    low = []
    for employee in all:
        if employee.pay_rate < avg_pay_rate:
            low.append(employee.name)
    return low
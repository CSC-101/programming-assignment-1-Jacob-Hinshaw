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



# Part 4


# Part 5


# Part 6


# Part 7


# Part 8



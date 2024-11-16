"""Coding exercise 15, 16, 17, 18, 19"""

# Coding Exercise 15:
"""
Squaring Numbers
You are going to write a List Comprehension to create a new list called squared_numbers. This new list should contain every number in the list numbers but each number should be squared. 

e.g.

4 * 4 = 16

4 squared equals 16.

**DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop. 

Target Output 

[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]

"""


def coding_exercise_15():
    input_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_list = [num ** 2 for num in input_list]
    print(squared_list)

# Coding Exercise_16():
    """
    Filtering Even Numbers
    In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.   
    
    
    
    First, use list comprehension to convert the list_of_strings to a list of integers called numbers.   
    
    Then use list comprehension again to create a new list called result.
    
    This new list should only contain the even numbers from the list numbers. 
    
    Again, try to use Python's List Comprehension instead of a Loop. 


    """


def coding_exercise_16():
    input_list = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    filtered_list = [num for num in input_list if int(num)%2==0]
    print(filtered_list)


"""
Data Overlap
💪 This exercise is HARD 💪 
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 
You are going to create a list called result which contains the numbers that are common in both files. 
e.g. if file1.txt contained: 
1 
2 
3
and file2.txt contained: 
2
3
4
result = [2, 3]
"""


def get_nums_from_str(input_str):
    proc_list = input_str.split("\n")

    return [int(num) for num in proc_list if num]


def data_overlap():
    with open("file1.txt", "r") as file1:
        file1_data = file1.read()
        file1_data_list = get_nums_from_str(file1_data)
        # print(file1_data_list)
    with open("file2.txt", "r") as file2:
        file2_data = file2.read()
        file2_data_list = get_nums_from_str(file2_data)
        # print(file2_data_list)
    res = [x for x in file1_data_list if x in file2_data_list]
    return res


#  Coding Exercise 18 Dictionary COmprehension
"""
Dictionary Comprehension 1
You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.   

Try Googling to find out how to convert a sentence into a list of words.  *

*Do NOT** Create a dictionary directly.

Try to use Dictionary Comprehension instead of a Loop. 

To keep this exercise simple, count any punctuation following a word with no whitespace as part of the word. Note that "Swallow?" therefore has a length of 8.
"""


def coding_exercise_18():
    str1 = "What is the Airspeed Velocity of an Unladen Swallow?"
    words = str1.split(" ")
    # print(words)
    words_dict = {word: len(word) for word in words}
    print(words_dict)


coding_exercise_15()
coding_exercise_16()
data_overlap()
coding_exercise_18()

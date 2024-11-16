def increment_by_one():
    numbers = [1, 2, 3]
    new_numbers = [x + 1 for x in numbers]
    print(new_numbers)


def str_to_char_arr():
    name = "Hussain Ahmed"
    new_name_letters = [char for char in name]
    print(new_name_letters)


def list_from_range():
    one_to_five = [2*x for x in range(1, 6)]
    print(one_to_five)


def list_using_conditions():
    """Conditional List comprehension"""
    # Syntax: new_list = [new_item for new_item in iterable if condition]
    even_nums = [x for x in range(1,101) if x%3==0]
    print(even_nums)


def list_using_conditions_1():
    """Conditional list comprehensions for capitalizing names whose len > 5"""
    names_list = ["Hussain", "Umair", "Shahika", "Gola", "Mahroof", "Ayan", "Adnan"]
    filter_names_list = [name.upper() for name in names_list if len(name) > 5]
    print(filter_names_list)


# Examples
increment_by_one()
str_to_char_arr()
list_from_range()
list_using_conditions()
list_using_conditions_1()


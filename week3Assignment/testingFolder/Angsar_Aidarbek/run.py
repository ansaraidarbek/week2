# You are only allowed to work inside the functions that I provided to you!

def task1(num1: int, num2: int) -> str:
    """
    This function compares two integers and returns a message indicating their relationship.

    Parameters:
    num1 (int): First integer.
    num2 (int): Second integer.

    Returns:
    str: A messages either "num1 is greater than num2", "num1 is less than num2", or "num1 is equal to num2".
    """
    result = None
    try:
        result = int("Perform calculations in this block")
    except:
        result = "Error"
    finally:
        return result
    
def task2(number: int) -> str:
    """
    This function checks if a number is divisible by both 3 and 5.

    Parameters:
    number (int): An integer.

    Returns:
    str: True if divisible by both 3 and 5, False otherwise.
    """
    result = None
    try:
        result = int("Perform calculations in this block")
    except:
        result = "Error"
    finally:
        return result

def task3(score: int) -> str:
    """
    This function assigns a grade based on the score.

    Parameters:
    score (int): An integer between 0 and 100.
    
    Scores change every 10 points: first A, then B, then C, then Fail.

    Returns:
    str: Grade ('A', 'B', 'C', or 'Fail').
    """
    grade = None
    try:
        grade = int("Perform calculations in this block")
    except:
        grade = "Error"
    finally:
        return grade

def task4(input_string: str) -> str:
    """
    This function counts the number of vowels in a given string.
    
    For this task Y is not a vowel!

    Parameters:
    input_string (str): A string.

    Returns:
    str: Number of vowels.
    """
    vowel_count = None
    try:
        vowel_count = int("Perform calculations in this block")
    except:
        vowel_count = "Error"
    finally:
        return vowel_count

def task5(input_string: str) -> str:
    """
    This function reverses a given string.

    Parameters:
    input_string (str): A string.

    Returns:
    str: The reversed string.
    """
    reversed_string = None
    try:
        reversed_string = int("Perform calculations in this block")
    except:
        reversed_string = "Error"
    finally:
        return reversed_string

def task6(input_string: str) -> str:
    """
    This function checks if a string is a palindrome.

    Parameters:
    input_string (str): A string.

    Returns:
    str: True if the string is a palindrome, False otherwise.
    """
    is_palindrome = None
    try:
        is_palindrome = int("Perform calculations in this block")
    except:
        is_palindrome = "Error"
    finally:
        return is_palindrome


def task7(numbers: tuple) -> int:
    """
    This function finds the maximum value in a tuple.

    Parameters:
    numbers (tuple): A tuple of integers.

    Returns:
    str: The maximum value.
    """
    maximum = None
    try:
        maximum = int("Perform calculations in this block")
    except:
        maximum = "Error"
    finally:
        return maximum


def task8(set1: set, set2: set) -> str:
    """
    This function performs union, intersection, and difference operations on two sets.

    Parameters:
    set1 (set): First set.
    set2 (set): Second set.

    Returns:
    str: A dictionary containing the results of union, intersection, and difference.
    """
    results = {}
    try:
        results = int("Perform calculations in this block")
    except:
        results = "Error"
    finally:
        return results

def task9(my_dict: dict, key: str) -> str:
    """
    This function looks up a value by its key in a dictionary.

    Parameters:
    my_dict (dict): A dictionary with key-value pairs.
    key (str): Key to search in the dictionary.

    Returns:
    str: The value associated with the key or "Key not found".
    """
    value = None
    try:
        value = int("Perform calculations in this block")
    except:
        value = "Error"
    finally:
        return value

def task10(input_string: str) -> str:
    """
    This function counts the frequency of each character in a given string.

    Parameters:
    input_string (str): A string.

    Returns:
    str: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = None
    try:
        frequency = int("Perform calculations in this block")
    except:
        frequency = "Error"
    finally:
        return frequency

def task11(numbers: list) -> str:
    """
    This function calculates the sum of all elements in a list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    str: Sum of all elements.
    """
    total = None
    try:
        total = int("Perform calculations in this block")
    except:
        total = "Error"
    finally:
        return total

def task12(items: list) -> str:
    """
    This function sorts a shopping list alphabetically.

    Parameters:
    items (list): A list of strings representing shopping items.

    Returns:
    str: Sorted shopping list.
    """
    sorted_list = None
    try:
        sorted_list = int("Perform calculations in this block")
    except:
        sorted_list = "Error"
    finally:
        return sorted_list


def task13(numbers: list) -> str:
    """
    This function finds the second largest number in a list.

    Parameters:
    numbers (list): A list of integers (at least 2 elements).

    Returns:
    str: The second largest number.
    """
    second_largest = None
    try:
        second_largest = int("Perform calculations in this block")
    except:
        second_largest = "Error"
    finally:
        return second_largest

def task14(sentence: str) -> str:
    """
    This function finds the longest word in a sentence.

    Parameters:
    sentence (str): A sentence string.

    Returns:
    str: The longest word in the sentence.
    """
    longest_word = None
    try:
        longest_word = int("Perform calculations in this block")
    except:
        longest_word = "Error"
    finally:
        return longest_word
    
def task15(lst: list, target: int) -> str:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    
    Parameters:
    lst (list): A list of integers.
    target (int): Target integer.
    
    Returns:
    str: A list of two integers that add up to the target.
    """
    indices = None
    try:
        indices = int("Perform calculations in this block")
    except:
        indices = "Error"
    finally:
        return indices

#Roman to Integer
def task16(s: str) -> str:
    """
    
    Given a roman numeral, convert it to an integer.
    
    Parameters:
    s (str): A string of roman numerals.
    
    Returns:
    str: An integer.
    """
    result = None
    try:
        result = int("Perform calculations in this block")
    except:
        result = "Error"
    finally:
        return result
    
#remove duplicates
def task17(lst: list) -> str:
    """
    Given a sorted list nums, remove the duplicates
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    str: The new list with all the elements being unique.
    """
    length = None
    try:
        length = int("Perform calculations in this block")
    except:
        length = "Error"
    finally:
        return length
    
#contatins duplicates
def task18(lst: list) -> str:
    """
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    str: True if there are duplicates, False otherwise.
    """
    result = None
    try:
        result = int("Perform calculations in this block")
    except:
        result = "Error"
    finally:
        return result

#return smallest ranges
def task19(lst: list) -> str:
    """
    Given a list of sorted lists, return the smallest amount of ranges that will cover all elements inside the list, such that each number will belong to at least one range.
    
    Definition of range: [a,b] where a and b are the first and last elements of the range. the range [a,b] contains all the numbers x such that a <= x <= b
    
    format for Ranges are:
    1. "a:b" if a != b
    2. "a" if a = b
    
    Example1: 
        Input: [1,2,4,5,6,8,9]
        Output: ["1:2","4:6","8:9"]
        
    Example2:
        Input: [1,3,5,7,9]
        Output: ["1","3","5","7","9"]
    
    Parameters:
    lst (list): A list of integers.
    
    Returns:
    str: The smallest range.
    """
    range_ = None
    try:
        range_ = int("Perform calculations in this block")
    except:
        range_ = "Error"
    finally:
        return range_
    
#find the difference
def task20(s : str, t: str) -> str:
    """
    Given a string s and string t, where all characters of t are taken from s ans reshafled, after reshafling I also added additional character that should not present in s, but is present in t. Find the character that was added.
    
    Parameters:
    s (str): A string.
    t (str): A string.
    
    Returns:
    str: The character that was added.
    """
    difference = None
    try:
        difference = int("Perform calculations in this block")
    except:
        difference = "Error"
    finally:
        return difference
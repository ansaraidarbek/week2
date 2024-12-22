# You are only allowed to work inside the functions that I provided to you!

def task1(num1: int, num2: int) -> str:
    """
    This function compares two integers and returns a message indicating their relationship.

    Parameters:
    num1 (int): First integer.
    num2 (int): Second integer.

    Returns:
    str: A message indicating whether num1 is greater, less, or equal to num2.
    """
    result = None
    try:
        if num1 > num2:
            result = "num1 is greater than num2"
        elif num1 < num2:
            result = "num1 is less than num2"
        else:
            result = "num1 is equal to num2"
    except:
        result = "Error"
    finally:
        return result
    
def task2(number: int) -> bool:
    """
    This function checks if a number is divisible by both 3 and 5.

    Parameters:
    number (int): An integer.

    Returns:
    bool: True if divisible by both 3 and 5, False otherwise.
    """
    result = None
    try:
        result = number % 3 == 0 and number % 5 == 0
    except:
        result = "Error"
    finally:
        return result

def task3(score: int) -> str:
    """
    This function assigns a grade based on the score.

    Parameters:
    score (int): An integer between 0 and 100.

    Returns:
    str: Grade ('A', 'B', 'C', or 'Fail').
    """
    grade = None
    try:
        if 90 <= score <= 100:
            grade = "A"
        elif 80 <= score < 90:
            grade = "B"
        elif 70 <= score < 80:
            grade = "C"
        else:
            grade = "Fail"
    except:
        grade = "Error"
    finally:
        return grade

def task4(input_string: str) -> int:
    """
    This function counts the number of vowels in a given string.

    Parameters:
    input_string (str): A string.

    Returns:
    int: Number of vowels.
    """
    vowel_count = None
    try:
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in input_string if char in vowels)
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
        reversed_string = input_string[::-1]
    except:
        reversed_string = "Error"
    finally:
        return reversed_string

def task6(input_string: str) -> bool:
    """
    This function checks if a string is a palindrome.

    Parameters:
    input_string (str): A string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    is_palindrome = None
    try:
        is_palindrome = input_string == input_string[::-1]
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
    int: The maximum value.
    """
    maximum = None
    try:
        maximum = max(numbers)
    except:
        maximum = "Error"
    finally:
        return maximum


def task8(set1: set, set2: set) -> dict:
    """
    This function performs union, intersection, and difference operations on two sets.

    Parameters:
    set1 (set): First set.
    set2 (set): Second set.

    Returns:
    dict: A dictionary containing the results of union, intersection, and difference.
    """
    results = None
    try:
        results = {
            "union": set1.union(set2),
            "intersection": set1.intersection(set2),
            "difference": set1.difference(set2)
        }
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
        value = my_dict.get(key, "Key not found")
    except:
        value = "Error"
    finally:
        return value

def task10(input_string: str) -> dict:
    """
    This function counts the frequency of each character in a given string.

    Parameters:
    input_string (str): A string.

    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = None
    try:
        frequency = {}
        for char in input_string:
            frequency[char] = frequency.get(char, 0) + 1
    except:
        frequency = "Error"
    finally:
        return frequency

def task11(numbers: list) -> int:
    """
    This function calculates the sum of all elements in a list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    int: Sum of all elements.
    """
    total = None
    try:
        total = sum(numbers)
    except:
        total = "Error"
    finally:
        return total

def task12(numbers: tuple) -> int:
    """
    This function finds the maximum value in a tuple.

    Parameters:
    numbers (tuple): A tuple of integers.

    Returns:
    int: The maximum value.
    """
    maximum = None
    try:
        maximum = max(numbers)
    except:
        maximum = "Error"
    finally:
        return maximum

def task13(set1: set, set2: set) -> dict:
    """
    This function performs union, intersection, and difference operations on two sets.

    Parameters:
    set1 (set): First set.
    set2 (set): Second set.

    Returns:
    dict: A dictionary containing the results of union, intersection, and difference.
    """
    results = None
    try:
        results = {
            "union": set1.union(set2),
            "intersection": set1.intersection(set2),
            "difference": set1.difference(set2)
        }
    except:
        results = "Error"
    finally:
        return results

def task14(my_dict: dict, key: str) -> str:
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
        value = my_dict.get(key, "Key not found")
    except:
        value = "Error"
    finally:
        return value

def task15(items: list) -> list:
    """
    This function sorts a shopping list alphabetically.

    Parameters:
    items (list): A list of strings representing shopping items.

    Returns:
    list: Sorted shopping list.
    """
    sorted_list = None
    try:
        sorted_list = sorted(items)
    except:
        sorted_list = "Error"
    finally:
        return sorted_list


def task16(input_string: str) -> dict:
    """
    This function counts the frequency of each character in a given string.

    Parameters:
    input_string (str): A string.

    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    frequency = None
    try:
        frequency = {}
        for char in input_string:
            frequency[char] = frequency.get(char, 0) + 1
    except:
        frequency = "Error"
    finally:
        return frequency
def task17(input_string: str) -> str:
    """
    This function reverses a given string.

    Parameters:
    input_string (str): A string.

    Returns:
    str: The reversed string.
    """
    reversed_string = None
    try:
        reversed_string = input_string[::-1]
    except:
        reversed_string = "Error"
    finally:
        return reversed_string
def task18(input_string: str) -> bool:
    """
    This function checks if a string is a palindrome.

    Parameters:
    input_string (str): A string.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    is_palindrome = None
    try:
        is_palindrome = input_string == input_string[::-1]
    except:
        is_palindrome = "Error"
    finally:
        return is_palindrome
def task19(numbers: list) -> int:
    """
    This function finds the second largest number in a list.

    Parameters:
    numbers (list): A list of integers (at least 2 elements).

    Returns:
    int: The second largest number.
    """
    second_largest = None
    try:
        if len(numbers) < 2:
            raise ValueError("List must have at least two elements")
        unique_numbers = list(set(numbers))  # Remove duplicates
        unique_numbers.sort(reverse=True)  # Sort in descending order
        second_largest = unique_numbers[1]  # Second largest
    except:
        second_largest = "Error"
    finally:
        return second_largest

def task20(sentence: str) -> str:
    """
    This function finds the longest word in a sentence.

    Parameters:
    sentence (str): A sentence string.

    Returns:
    str: The longest word in the sentence.
    """
    longest_word = None
    try:
        words = sentence.split()
        longest_word = max(words, key=len)
    except:
        longest_word = "Error"
    finally:
        return longest_word

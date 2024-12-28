import traceback
import json

def test_task1(_, module):
    try:
        inputs = [(10, 5), (2, 2), (0, 10)]
        expected = [
            "num1 is greater than num2",
            "num1 is equal to num2",
            "num1 is less than num2"
        ]
        for (num1, num2), exp in zip(inputs, expected):
            result = module.task1(num1, num2)
            if result != exp:
                return False, f"Input: {(num1, num2)}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task2(_, module):
    try:
        inputs = [15, 30, 7, 10]
        expected = ["True", "True", "False", "False"]
        for inp, exp in zip(inputs, expected):
            result = module.task2(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task3(_, module):
    try:
        inputs = [95, 82, 74, 70]
        expected = ["A", "B", "C", "Fail"]
        for inp, exp in zip(inputs, expected):
            result = module.task3(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task4(_, module):
    try:
        inputs = ["hello", "world", "AEIOU", "python"]
        expected = ["2", "1", "5", "1"]
        for inp, exp in zip(inputs, expected):
            result = module.task4(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task5(_, module):
    try:
        inputs = ["hello", "python", "123", "abc"]
        expected = ["olleh", "nohtyp", "321", "cba"]
        for inp, exp in zip(inputs, expected):
            result = module.task5(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task6(_, module):
    try:
        inputs = ["racecar", "madam", "hello", "abcba"]
        expected = ["True", "True", "False", "True"]
        for inp, exp in zip(inputs, expected):
            result = module.task6(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task7(_, module):
    try:
        inputs = [(1, 2, 3), (10, 5, 6), (-1, -5, 0)]
        expected = ["3", "10", "0"]
        for inp, exp in zip(inputs, expected):
            result = module.task7(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task8(_, module):
    try:
        inputs = [({1, 2, 3}, {3, 4}), (set(), {1, 2}), ({5, 6}, {7})]
        expected = [
            {"union": {1, 2, 3, 4}, "intersection": {3}, "difference": {1, 2}},
            {"union": {1, 2}, "intersection": set(), "difference": set()},
            {"union": {5, 6, 7}, "intersection": set(), "difference": {5, 6}}
        ]
        for (set1, set2), exp in zip(inputs, expected):
            result = module.task8(set1, set2)
            if result != str(exp):
                print("I am returning", set1, set2, exp)
                return False, f"Input: {(set1, set2)}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

    
def test_task9(_, module):
    try:
        inputs = [({"a": 1, "b": 2}, "a"), ({"x": 10}, "y"), ({}, "z")]
        expected = ["1", "Key not found", "Key not found"]
        for (my_dict, key), exp in zip(inputs, expected):
            result = module.task9(my_dict, key)
            if result != exp:
                return False, f"Input: {(my_dict, key)}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task10(_, module):
    try:
        inputs = ["hello", "world", "aabbcc", ""]
        expected = [
            {"h": 1, "e": 1, "l": 2, "o": 1},
            {"w": 1, "o": 1, "r": 1, "l": 1, "d": 1},
            {"a": 2, "b": 2, "c": 2},
            {}
        ]
        for inp, exp in zip(inputs, expected):
            result = module.task10(inp)
            if result != str(exp):
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task11(_, module):
    try:
        inputs = [[1, 2, 3], [10, -5, 5], [0, 0, 0], []]
        expected = ["6", "10", "0", "0"]
        for inp, exp in zip(inputs, expected):
            result = module.task11(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task12(_, module):
    try:
        inputs = [["banana", "apple", "cherry"], ["c", "a", "b"], [], ["z"]]
        expected = [
            ["apple", "banana", "cherry"],
            ["a", "b", "c"],
            [],
            ["z"]
        ]
        for inp, exp in zip(inputs, expected):
            result = module.task12(inp)
            if result != str(exp):
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task13(_, module):
    try:
        inputs = [[10, 20, 30], [1, 2, 3, 4], [-5, -10, 0]]
        expected = ["20", "3", "-5"]
        for inp, exp in zip(inputs, expected):
            result = module.task13(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task14(_, module):
    try:
        inputs = ["This are tests", "hello worlds", "python programming"]
        expected = ["tests", "worlds", "programming"]
        for inp, exp in zip(inputs, expected):
            result = module.task14(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task15(_, module):
    try:
        inputs = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
            ([1, 2, 3, 4, 6], 10)
        ]
        expected = [
            "[0, 1]",
            "[1, 2]",
            "[0, 1]",
            "[3, 4]"
        ]
        for (lst, target), exp in zip(inputs, expected):
            result = module.task15(lst, target)
            if result != exp:
                return False, f"Input: {lst}, Target: {target}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task16(_, module):
    try:
        inputs = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
        expected = ["3", "4", "9", "58", "1994"]
        for inp, exp in zip(inputs, expected):
            result = module.task16(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task17(_, module):
    try:
        inputs = [[1, 1, 2], [0, 0, 1, 1, 2, 2], [], [5, 5, 5]]
        expected = [
            "[1, 2]",
            "[0, 1, 2]",
            "[]",
            "[5]"
        ]
        for inp, exp in zip(inputs, expected):
            result = module.task17(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task18(_, module):
    try:
        inputs = [[1, 2, 3, 1], [1, 2, 3, 4], [0, 0, 0], []]
        expected = ["True", "False", "True", "False"]
        for inp, exp in zip(inputs, expected):
            result = module.task18(inp)
            if result != exp:
                return False, f"Input: {inp}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"
    
def test_task19(_, module):
    try:
        inputs = [[1, 2, 4, 5, 6, 8, 9], [1, 3, 5, 7, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
        expected_A = [
            '["1:2", "4:6", "8:9"]',
            '["1", "3", "5", "7", "9"]',
            '["1:9"]'
        ]
        expected_B = [
            "['1:2', '4:6', '8:9']",
            "['1', '3', '5', '7', '9']",
            "['1:9']"
        ]
        for inp, expA, expB in zip(inputs, expected_A, expected_B):
            result = module.task19(inp)
            if result != expA and result != expB:
                return False, f"Input: {inp}, Expected: {expA}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

def test_task20(_, module):
    try:
        inputs = [("abcd", "abcde"), ("a", "aa"), ("", "y"), ("abc", "abc1")]
        expected = ["e", "a", "y", "1"]
        for (s, t), exp in zip(inputs, expected):
            result = module.task20(s, t)
            if result != exp:
                return False, f"Input: {(s, t)}, Expected: {exp}, Got: {result}"
        return True, "All test cases passed"
    except Exception as e:
        return False, f"Error: {traceback.format_exc()}"

    

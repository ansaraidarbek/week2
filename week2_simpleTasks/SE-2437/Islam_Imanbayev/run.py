def task1(initialString: str) -> str:
    newString = None
    try:
        newString = initialString + " Your Name"
    except:
        newString = "Error"
    finally:
        return newString

def task2(value: int) -> str:
    result = None
    try:
        result = str(value * 4 + 20)
    except:
        result = "Error"
    finally:
        return result

def task3(age: int) -> str:
    is_eligible = None
    try:
        is_eligible = str(age >= 18)
    except:
        is_eligible = "Error"
    finally:
        return is_eligible

def task4(number: int) -> str:
    result = None
    try:
        result = "Even" if number % 2 == 0 else "Odd"
    except:
        result = "Error"
    finally:
        return result

def task5(s: str) -> str:
    result = None
    try:
        result = s[::-1] + str(len(s))
    except:
        result = "Error"
    finally:
        return result

def task6(n: int) -> str:
    result = None
    try:
        result = str(n * (n + 1) // 2)
    except:
        result = "Error"
    finally:
        return result

def task7(n: int) -> str:
    freq = None
    try:
        num_str = str(n)
        freq = {digit: num_str.count(digit) for digit in num_str}
        freq = str(freq)
    except:
        freq = "Error"
    finally:
        return freq

def task8(password: str) -> str:
    is_valid = None
    try:
        is_valid = str(len(password) >= 8 and any(char.isdigit() for char in password))
    except:
        is_valid = "Error"
    finally:
        return is_valid

def task9(n: int) -> str:
    result = None
    try:
        if n > 1:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    result = "False"
                    break
            else:
                result = "True"
        else:
            result = "False"
    except:
        result = "Error"
    finally:
        return result

def task10(numbers: list) -> str:
    result = None
    try:
        result = str(sum(numbers))
    except:
        result = "Error"
    finally:
        return result

def task11(s: str) -> str:
    result = None
    try:
        result = s.upper()
    except:
        result = "Error"
    finally:
        return result

def task12(s: str) -> str:
    result = None
    try:
        result = s.lower()
    except:
        result = "Error"
    finally:
        return result

def task13(s: str) -> str:
    result = None
    try:
        result = str(s == s[::-1])
    except:
        result = "Error"
    finally:
        return result

def task14(numbers: list) -> str:
    result = None
    try:
        result = str(max(numbers))
    except:
        result = "Error"
    finally:
        return result

def task15(numbers: list) -> str:
    result = None
    try:
        result = str(min(numbers))
    except:
        result = "Error"
    finally:
        return result

def task16(n: int) -> str:
    result = None
    try:
        result = str(n ** 2)
    except:
        result = "Error"
    finally:
        return result

def task17(numbers: list) -> str:
    result = None
    try:
        result = str(sorted(numbers))
    except:
        result = "Error"
    finally:
        return result

def task18(numbers: list) -> str:
    result = None
    try:
        result = str(sorted(numbers, reverse=True))
    except:
        result = "Error"
    finally:
        return result

def task19(a: int, b: int) -> str:
    result = None
    try:
        result = str(a + b)
    except:
        result = "Error"
    finally:
        return result

def task20(a: int, b: int) -> str:
    result = None
    try:
        result = str(a * b)
    except:
        result = "Error"
    finally:
        return result
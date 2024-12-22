def prerequisites() -> bool:
    """
    Are you willing to submit this lesson, if yes then change to True?

    Returns:
        bool: True or False.
    """
    return True


def task1(initialString: str) -> str:
    try:
        newString = initialString + "Ibrahim Nygyman"
    except:
        newString = "Error"
    finally:
        return newString


def task2(val: int) -> str:
    try:
        result = str(val * 4 + 20)
    except:
        result = "Error"
    finally:
        return result


def task3(age: int) -> str:
    try:
        is_eligible = str(age >= 18)
    except:
        is_eligible = "Error"
    finally:
        return is_eligible


def task4(number: int) -> str:
    try:
        result = "Even" if number % 2 == 0 else "Odd"
    except:
        result = "Error"
    finally:
        return result


def task5(s: str) -> str:
    try:
        result = s[::-1] + str(len(s))
    except:
        result = "Error"
    finally:
        return result


def task6(n: int) -> str:
    try:
        result = str(n * (n + 1) // 2)
    except:
        result = "Error"
    finally:
        return result

def task8(password: str) -> str:
    try:
        is_valid = str(len(password) >= 8 and any(char.isdigit() for char in password))
    except:
        is_valid = "Error"
    finally:
        return is_valid


def task9(n: int) -> str:
    try:
        result = str(all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))) if n > 1 else "False"
    except:
        result = "Error"
    finally:
        return result


def task10(n: int) -> str:
    try:
        result = str(str(n) == str(n)[::-1])
    except:
        result = "Error"
    finally:
        return result


def task11(start: int, end: int) -> str:
    try:
        count = str(len([i for i in range(start, end + 1) if i % 5 == 0]))
    except:
        count = "Error"
    finally:
        return count


def task12(a: int, b: int) -> str:
    try:
        is_greater = str(a + b > 50)
    except:
        is_greater = "Error"
    finally:
        return is_greater


def task13(a: int, b: int, c: int) -> str:
    try:
        largest = str(max(a, b, c))
    except:
        largest = "Error"
    finally:
        return largest


def task14(number: int) -> str:
    try:
        result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
    except:
        result = "Error"
    finally:
        return result


def task15(a: int, b: int) -> str:
    try:
        result = str(a % b == 0)
    except:
        result = "Error"
    finally:
        return result


def task16(first: int, second: int, third: int) -> str:
    try:
        result = str(
            first**2 + second**2 == third**2
            or second**2 + third**2 == first**2
            or third**2 + first**2 == second**2
        )
    except:
        result = "Error"
    finally:
        return result


def task17(number: int) -> str:
    try:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        result = str(factorial)
    except:
        result = "Error"
    finally:
        return result


def task18() -> str:
    try:
        answer = str(7)
    except:
        answer = "Error"
    finally:
        return answer


def task19(x: int) -> str:
    try:
        result = str(sum(i for i in range(1, x + 1) if i % 2 == 0))
    except:
        result = "Error"
    finally:
        return result


def task20(secret_number: int, guess: int) -> str:
    try:
        if guess > secret_number:
            result = "Too High"
        elif guess < secret_number:
            result = "Too Low"
        else:
            result = "Correct!"
    except:
        result = "Error"
    finally:
        return result
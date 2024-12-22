def prerequisites() -> bool:
    """
    Are you willing to submit this lesson, if yes then change to True?

    Returns:
        bool: True or False.
    """
    return True


# You are only allowed to work inside the functions that I provided to you!

def task1(initialString: str) -> str:
    """
    This function should return the updated string by adding your fullName to it.

    Parameters:
    initialString (str): some random string.

    Returns:
    str: updated string.
    """
    newString = None
    # Perform the task below, change the code inside the try block.:
    try:
        newString = f"{str}Mukhammad Sarah"
    except:
        newString = "Error"
    finally:
        return newString


def task2(val: int) -> str:
    """
    Perform a calculation: multiply input by 4 and add 20 to the result.
    Return the final value.

    Parameters:
    val (int) : a random real nubmer

    Returns:
    str: result of the calculation.
    """
    result = None

    # Perform the task below, change the code inside the try block.:
    try:
        # Even though the result is int, you should return it as a string.
        result = str(val * 4 + 20)
    except:
        result = "Error"
    finally:
        return result


def task3(age: int) -> str:
    """
    Check if the given age is eligible for voting (age >= 18).

    Parameters:
    age (int): age of a person.

    Returns:
    str: True if eligible, False otherwise.
    """
    is_eligible = False
    # Perform the task below, change the code inside the try block.:
    try:
        if(age >= 18):
            is_eligible = True
    except:
        is_eligible = "Error"
    finally:
        return is_eligible


def task4(number: int) -> str:
    """
    Check if the given number is even or odd.

    Parameters:
    number (int): a number to check.

    Returns:
    str: "Even" if the number is even, "Odd" if it is odd.
    """
    result = None
    # Perform the task below, change the code inside the try block.:
    try:
        if(number % 2 == 0):
            result = "Even"
        else:
            result = "Odd"
    except:
        result = "Error"
    finally:
        return result


def task5(s: str) -> str:
    """
    Reverse the input string and append its length at the end.
    Example: "hello" -> "olleh5"
    Example2: "world" -> "dlrow5"

    Parameters:
    s (str): the input string.

    Returns:
    str: the reversed string with its length appended.
    """
    result = None
    # Hint: use a len() function to get the length of the string.

    # Perform the task below, change the code inside the try block.:
    try:
        result = f"{s[::-1]}{len(s)}"
    except:
        result = "Error"
    finally:
        return result


def task6(n: int) -> str:
    """
    Calculate the sum of the first n natural numbers.

    Parameters:
    n (int): number of terms.

    Returns:
    str: sum of the first n natural numbers.
    """
    try:
        # Calculate the sum using the formula for the sum of first n natural numbers
        result = n * (n + 1) // 2
        return str(result)
    except Exception as e:
        return "Error"


def task7(n: int) -> str:
    """
    Count the frequency of each digit in a number.
    Example: 12234 -> one1two2three1four1
    Example2: 13235 -> one1two1three2five1

    Parameters:
    n (int): the input number.

    Returns:
    str: a string with the frequencies of digits in the format "wordfrequency".
    """
    # A mapping of digits to their corresponding English words
    digit_words = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    try:
        # Convert the number to a string to easily iterate over each digit
        num_str = str(n)

        # Initialize a dictionary to count the frequency of each digit
        digit_count = {}

        for digit in num_str:
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1

        # Create the result string in the required format
        result = ""
        for digit in sorted(digit_count.keys()):
            result += f"{digit_words[digit]}{digit_count[digit]}"

        return result
    except Exception as e:
        return "Error"

def task8(password: str) -> str:
    """
    Check if the given password meets the criteria:
    - At least 8 characters long.
    - Contains at least one digit.

    Parameters:
    password (str): the password to check.

    Returns:
    str: "True" if the password meets the criteria, "False" otherwise.
    """

    try:
        # Check if password is at least 8 characters long
        if len(password) >= 8 and any(char.isdigit() for char in password):
            return "True"
        else:
            return "False"
    except Exception as e:
        return "Error"


def task9(n: int) -> str:
    """
    Check if the given number is a prime number.

    Parameters:
    n (int): a positive number to check.

    Returns:
    str: "True" if the number is prime, "False" otherwise.
    """
    try:
        # Check if n is less than 2 (as 0 and 1 are not prime numbers)
        if n < 2:
            return "False"

        # Check divisibility from 2 to sqrt(n) to optimize the process
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return "False"  # Divisible by i, not prime

        return "True"  # Prime if no divisors found
    except Exception as e:
        return "Error"


def task10(n: int) -> str:
    """
    Check if the given number is a palindrome.

    Parameters:
    n (int): a number to check.

    Returns:
    str: "True" if the number is a palindrome, "False" otherwise.
    """
    try:
        # Convert the number to a string
        num_str = str(n)

        # Check if the string is equal to its reverse
        if num_str == num_str[::-1]:
            return "True"
        else:
            return "False"
    except Exception as e:
        return "Error"


def task11(start: int, end: int) -> str:
    """
    Count how many numbers between start and end (inclusive) are divisible by 5.

    Parameters:
    start (int): start of the range.
    end (int): end of the range.

    Returns:
    str: count of numbers divisible by 5.
    """
    try:
        # Initialize the count
        count = 0

        # Loop through the range from start to end (inclusive)
        for num in range(start, end + 1):
            if num % 5 == 0:
                count += 1

        return str(count)
    except Exception as e:
        return "Error"


def task12(a: int, b: int) -> str:
    """
    Check if two numbers satisfy the condition: their sum is greater than 50.

    Parameters:
    a (int): first number.
    b (int): second number.

    Returns:
    str: "True" if the sum is greater than 50, "False" otherwise.
    """
    try:
        is_greater = (a + b) > 50
        return "True" if is_greater else "False"
    except:
        return "Error"


def task13(a: int, b: int, c: int) -> str:
    """
    Return the largest number among three numbers.

    Parameters:
    a (int): first number.
    b (int): second number.
    c (int): third number.

    Returns:
    str: the largest number.
    """
    try:
        largest = max(a, b, c)
        return str(largest)
    except:
        return "Error"


def task14(number: int) -> str:
    """
    Check if a number is positive, negative, or zero.

    Parameters:
    number (int): a number to check.

    Returns:
    str: "Positive", "Negative", or "Zero".
    """
    try:
        if number > 0:
            return "Positive"
        elif number < 0:
            return "Negative"
        else:
            return "Zero"
    except:
        return "Error"


def task15(a: int, b: int) -> str:
    """
    Check if the first number is divisible by the second number.

    Parameters:
    a (int): first number.
    b (int): second number.

    Returns:
    str: "True" if a is divisible by b, otherwise "False".
    """
    try:
        is_divisible = a % b == 0
        return "True" if is_divisible else "False"
    except:
        return "Error"

def task16(first: int, second: int, third: int) -> str:
    """
    Check if the numbers form a Pythagorean triplet.

    Parameters:
    first (int): first side.
    second (int): second side.
    third (int): third side.

    Returns:
    str: "True" if the numbers form a Pythagorean triplet, otherwise "False".
    """
    try:
        sides = sorted([first, second, third])
        is_triplet = sides[0]**2 + sides[1]**2 == sides[2]**2
        return "True" if is_triplet else "False"
    except:
        return "Error"


def task17(number: int) -> str:
    """
    Calculate the factorial of a number using a loop.

    Parameters:
    number (int): the number to calculate the factorial for.

    Returns:
    str: the factorial of the number.
    """
    try:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        return str(factorial)
    except:
        return "Error"


def task18() -> str:
    """
    Solve a riddle using logical operators:
    I am a single digit. I am greater than 5 but less than 9, and I am odd. What number am I?

    Returns:
    str: the answer to the riddle.
    """
    try:
        # The number that is greater than 5, less than 9, and odd is 7.
        answer = 7
        return str(answer)
    except:
        return "Error"


def task19(x: int) -> str:
    """
    Use a loop to calculate the sum of all even numbers from 1 to x (inclusive).

    Parameters:
    x (int): the upper limit.

    Returns:
    str: the sum of all even numbers from 1 to x.
    """
    try:
        total = 0
        for num in range(2, x + 1, 2):
            total += num
        return str(total)
    except:
        return "Error"

def task20(secret_number: int, guess: int) -> str:
    """
    Guess the Secret Number!
    - The secret number is between 1 and 100.
    - Compare the guessed number with the secret number and give hints:
      - "Too High" if the guess is greater than the secret number.
      - "Too Low" if the guess is less than the secret number.
      - "Correct!" if the guess matches the secret number.

    Parameters:
    secret_number (int): the secret number (between 1 and 100).
    guess (int): the guessed number.

    Returns:
    str: "Too High", "Too Low", or "Correct!".
    """
    try:
        if guess > secret_number:
            return "Too High"
        elif guess < secret_number:
            return "Too Low"
        else:
            return "Correct!"
    except:
        return "Error"

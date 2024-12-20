# You are only allowed to work inside the functions that I provided to you!

def prerequisites () :
    """
        Are you willing to submit this lesson, if yes then change to True?

        Returns:
            bool: True or False.
    """
    return True

def task1 (initialString: str) -> str:
    """
    This function should return the updated string by adding your fullName to it.

    Parameters:
    initialString (str): some random string.

    Returns:
    str: updated string.
    """
    newString = None
    # Perform the task below, change the code inside the try block.:
    try : 
        newString = initialString + " Almat Muzdybay "
    except: 
        newString = "Error"
    finally:
        return newString

def task2(val : int) -> str:
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
    try : 
        # Even though the result is int, you should return it as a string.
        result = str(val*4+20)
    except:
        result= "Error"
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
    is_eligible = None
    # Perform the task below, change the code inside the try block.:
    try : 
        is_eligible = str(age>=18)
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
    try : 
        result = "Odd" if number % 2 == 1 else "Even"
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
    #Hint: use a len() function to get the length of the string.
    
    # Perform the task below, change the code inside the try block.:
    try : 
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
    # Hint: https://www.geeksforgeeks.org/sum-of-natural-numbers/
    result = None
    # Perform the task below, change the code inside the try block.:
    try : 
        result = str(n*(n+1)//2)
    except:
        result = "Error"
    finally:
        return result
    
def task7(n: int) -> str:
    """
    Count the frequency of each digit in a number.
    Example: 12234 -> one1two2three1four1
    Example2: 13235 -> one1two1three2five1

    Parameters:
    n (int): the input number.

    Returns:
    str: a dictionary with digits as keys and their frequencies as values.
    """
    freq = None
    # Perform the task below, change the code inside the try block.:
    try : 
        #freq = int("Count the frequency of each digit in the number")
        num_str=str(n)
        dict_w_digits = {
			"1": "one",
			"2": "two",
			"3": "three",
			"4": "four",
			"5": "five",
			"6": "six",
			"7": "seven",
			"8": "eight",
			"9": "nine",
			"0": "zero"
		}
        for digit in sorted(set(num_str),key=num_str.index):
            count = num_str.count(digit)
            freq += f"{dict_w_digits[digit]}{count}"
        return freq
    except:
        freq="Error"
    finally:
        return freq

def task8(password: str) -> str:
    """
    Check if the given password meets the criteria:
    - At least 8 characters long.
    - Contains at least one digit.

    Parameters:
    password (str): the password to check.

    Returns:
    str: True if the password meets the criteria, False otherwise.
    """

    # Hint: use loop to iterate over the characters of the password.
    is_valid = None
    # Perform the task below, change the code inside the try block.:
    try : 
        count_digit=0
        for char in password:
            if char.isdigit():
                count_digit+=1
        if len(password) >= 8 and count_digit>=1:
            is_valid = "True"
        else:
            is_valid = "False"
    except:
        is_valid = "Error"
    finally:
        return is_valid
    
def task9(n: int) -> str:
    """
    Check if the given number is a prime number.

    Parameters:
    n (int): a positive number to check.

    Returns:
    str: True if the number is prime, False otherwise.
    """
    result = None
    # Hint: try to devide the number by all numbers from 2 to n-1, if it is divisible by any of them, then it is not a prime number.

    # Perform the task below, change the code inside the try block.:
    try : 
        if n <= 1:
            return False
        for i in range(2, n-1): 
            if n % i == 0:
                result = False  
                break
        else:
            result = "True"
    except:
        result = "Error"
    finally:
        return result

def task10(n: int) -> str:
    """
    Check if the given number is a palindrome.

    Parameters:
    n (int): a number to check.

    Returns:
    str: True if the number is palindrome, False otherwise.
    """
    result = None
    # Hint: convert the number to a string and check if it is equal to its reverse.

    # Perform the task below, change the code inside the try block.:
    try : 
        str_num=str(n)
        result = "True" if str_num==str_num[::-1] else "False"
    except:
        result = "Error"
    finally:
        return result
    
def task11(start: int, end: int) -> str:
    """
    Count how many numbers between start and end (inclusive) are divisible by 5.

    Parameters:
    start (int): start of the range.
    end (int): end of the range.

    Returns:
    str: count of numbers divisible by 5.
    """
    count = None
    # Perform the task below, change the code inside the try block.:
    try : 
        count = str(sum(i % 5 == 0 for i in range(start, end+1)))

    except:
        count = "Error"
    finally:
        return count
    
def task12(a: int, b: int) -> str:
    """
    Check if two numbers satisfy the condition: their sum is greater than 50.

    Parameters:
    a (int): first number.
    b (int): second number.

    Returns:
    str: True if the sum is greater than 50, False otherwise.
    """
    is_greater = None
    # Perform the task below, change the code inside the try block.:
    try : 
        is_greater = str((a+b)>50)
    except:
        is_greater = "Error"
    finally:
        return is_greater
    
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
    largest = None
    # Perform the task below, change the code inside the try block.:
    try : 
        largest = str(max(a,b,c))
    except:
        largest = "Error"
    finally:
        return largest
    
def task14(number: int) -> str:
    """
    Check if a number is positive, negative, or zero.

    Parameters:
    number (int): a number to check.

    Returns:
    str: "Positive", "Negative", or "Zero".
    """
    result = None
    # Perform the task below, change the code inside the try block.:
    try : 
        if number>0:
            result="Positive"
        elif number<0:
            result="Negative"
        else:
            result="Zero"
    except:
        result = "Error"
    finally:
        return result
    
def task15(a: int, b: int) -> str:
    """
    Check if the first number is divisible by the second number.

    Parameters:
    a (int): first number.
    b (int): second number.

    Returns:
    str: "True" if a is divisible by b, otherwise "False".
    """
    result = None
    # Perform the task below, change the code inside the try block.:
    try : 
        result = str(a % b == 0)
    except:
        result = "Error"
    finally:
        return result
    
def task16(first: int, second: int, third: int) -> str:
    """
    Check if the numbers form a Pythagorean triplet.

    Parameters:
    first (int): first side.
    secodn (int): second side.
    third (int): third side.

    Returns:
    str: "True" if the numbers form a Pythagorean triplet, otherwise "False".
    """
    result = None
    # Hint: Pythagorean theorem: x^2 + y^2 = z^2
    # Hint2: Pythagorean triplet is a set of three integers a, b, and c such that a^2 + b^2 = c^2.
    
    # Perform the task below, change the code inside the try block.:
    try : 
        sides = sorted([first, second, third])
        if sides[0]**2 + sides[1]**2 == sides[2]**2:
            result="True"
        else:
            result="False"
    except:
        result = "Error"
    finally:
        return result
    
def task17(number: int) -> str:
    """
    Calculate the factorial of a number using a loop.

    Parameters:
    number (int): the number to calculate the factorial for.

    Returns:
    int: the factorial of the number.
    """

    # Hint: use the loop to multiply the number by all numbers less than it.
    factorial = None
    # Perform the task below, change the code inside the try block.:
    try : 
        factorial=1
        for i in range(1,number+1):
            factorial*=i
        factorial = str(factorial)
    except:
        factorial = "Error"
    finally:
        return factorial

def task18() -> str:
    """
    Solve a riddle using logical operators: 
    I am a single digit. I am greater than 5 but less than 9, and I am odd. What number am I?

    Returns:
    str: the answer to the riddle.
    """
    answer = None
    # Perform the task below, change the code inside the try block.:
    try : 
        answer = "7"
    except:
        answer = "Error"
    finally:
        return answer
    
def task19(x: int) -> str:
    """
    Use a loop to calculate the sum of all even numbers from 1 to x (inclusive).

    Parameters:
    x (int): the upper limit.

    Returns:
    str: the sum of all even numbers from 1 to x.
    """
    result = None
    # Perform the task below, change the code inside the try block.:
    try : 
        sum=0
        for i in range(2,x+1,2):
            sum+=i
        result=str(sum)
    except:
        result = "Error"
    finally:
        return result

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
    result = None

    # Perform the task below, change the code inside the try block.:
    try : 
        if guess>secret_number:
            result="Too High"
        elif guess<secret_number:
            result="Too Low"
        else:
            result="Correct!"
    except:
        result = "Error"
    finally:
        return result    
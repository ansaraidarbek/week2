def prereq() -> bool:
    """
    Check if ready to submit.

    Returns:
        bool: True or False.
    """
    return True

def t1(s: str) -> str:
    try:
        res = s + " Ardak Avissauly"
    except:
        res = "Error"
    return res

def t2(x: int) -> str:
    try:
        res = str(x * 4 + 20)
    except:
        res = "Error"
    return res

def t3(age: int) -> str:
    try:
        res = str(age >= 18)
    except:
        res = "Error"
    return res

def t4(num: int) -> str:
    try:
        res = "Even" if num % 2 == 0 else "Odd"
    except:
        res = "Error"
    return res

def t5(s: str) -> str:
    try:
        res = s[::-1] + str(len(s))
    except:
        res = "Error"
    return res

def t6(n: int) -> str:
    try:
        res = str(n * (n + 1) // 2)
    except:
        res = "Error"
    return res

def t8(pw: str) -> str:
    try:
        res = str(len(pw) >= 8 and any(ch.isdigit() for ch in pw))
    except:
        res = "Error"
    return res

def t9(n: int) -> str:
    try:
        res = str(all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))) if n > 1 else "False"
    except:
        res = "Error"
    return res

def t10(n: int) -> str:
    try:
        res = str(str(n) == str(n)[::-1])
    except:
        res = "Error"
    return res

def t11(a: int, b: int) -> str:
    try:
        res = str(sum(1 for i in range(a, b + 1) if i % 5 == 0))
    except:
        res = "Error"
    return res

def t12(a: int, b: int) -> str:
    try:
        res = str(a + b > 50)
    except:
        res = "Error"
    return res

def t13(a: int, b: int, c: int) -> str:
    try:
        res = str(max(a, b, c))
    except:
        res = "Error"
    return res

def t14(n: int) -> str:
    try:
        res = "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
    except:
        res = "Error"
    return res

def t15(a: int, b: int) -> str:
    try:
        res = str(a % b == 0)
    except:
        res = "Error"
    return res

def t16(a: int, b: int, c: int) -> str:
    try:
        res = str(
            a ** 2 + b ** 2 == c ** 2 or
            b ** 2 + c ** 2 == a ** 2 or
            c ** 2 + a ** 2 == b ** 2
        )
    except:
        res = "Error"
    return res

def t17(n: int) -> str:
    try:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        res = str(fact)
    except:
        res = "Error"
    return res

def t18() -> str:
    try:
        res = str(7)
    except:
        res = "Error"
    return res

def t19(x: int) -> str:
    try:
        res = str(sum(i for i in range(1, x + 1) if i % 2 == 0))
    except:
        res = "Error"
    return res

def t20(secret: int, guess: int) -> str:
    try:
        if guess > secret:
            res = "Too High"
        elif guess < secret:
            res = "Too Low"
        else:
            res = "Correct!"
    except:
        res = "Error"
    return res

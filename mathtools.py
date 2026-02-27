# math_tools.py

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def is_even(n):
    return n % 2 == 0

def subtract(a, b):
    return a - b

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
def is_palindrome(a):
    sanitized = a.replace(" ", "")
    return sanitized == sanitized[::-1]

def find_min(numbers):
    if not numbers:
        return None
    
    min_val = numbers[0]
    
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def remove_duplicates(items):
    result = []
    
    for item in items:
        if item not in result:
            result.append(item)
            
    return result
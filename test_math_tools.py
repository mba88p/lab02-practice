# test_math_tools.py
from mathtools import add, multiply, is_even, subtract, max_of_three, is_palindrome, find_min, remove_duplicates

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("test_add: ALL PASSED")
    
def test_multiply():
    assert multiply (3, 4) == 12
    assert multiply (-2, 5) == -10
    assert multiply (0, 100) == 0
    print ("test_multiply: ALL PASSED")

def test_is_even():
    assert is_even (4) == True
    assert is_even (7) == False
    assert is_even (0) == True
    print (" test_is_even : ALL PASSED ")

def test_subtract():
    assert subtract(5, 4) == 1
    assert subtract(1, -2) == 3
    assert subtract(0, 0) == 0
    
def test_max_of_three():
    assert max_of_three(0, 1, 2) == 2
    assert max_of_three(0, 3, 1) == 3
    assert max_of_three(4, 2, 1) == 4
    assert max_of_three(4, 4, 5) == 5
    assert max_of_three(3, 3, 3) == 3

def test_is_palindrome():
    assert is_palindrome("race car") == True 
    assert is_palindrome("Race car") == False
    assert is_palindrome("12321") == True
    assert is_palindrome("apple") == False
    assert is_palindrome("step on no pets") == True
    assert is_palindrome("  ") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_find_min():
    assert find_min([5, 10, 15]) == 5
    assert find_min([-10, -20, -5]) == -20
    assert find_min([-1, 0, 1]) == -1
    assert find_min([42]) == 42
    assert find_min([7, 2, 2, 8]) == 2
    assert find_min([]) is None

def test_remove_duplicates():
    assert remove_duplicates([]) == []
    assert remove_duplicates([10, 20, 30]) == [10, 20, 30]
    assert remove_duplicates(["a", "a", "a"]) == ["a"]
    assert remove_duplicates([1, "1", 2]) == [1, "1", 2]
    assert remove_duplicates([5, 1, 5, 2, 1]) == [5, 1, 2]
    nested = [[1, 2], [1, 2], [3]]
    assert remove_duplicates(nested) == [[1, 2], [3]]
    
# Run all tests
test_add()
test_subtract()
test_multiply()
test_is_even()
test_max_of_three()
test_is_palindrome()
test_find_min()
test_remove_duplicates()

print (" --- All tests passed ! ---")
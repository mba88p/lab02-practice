# test_math_tools.py
from mathtools import add, multiply, is_even

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

# Run all tests
test_add()
test_multiply()
test_is_even()
print (" --- All tests passed ! ---")
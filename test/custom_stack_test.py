import pytest
from custom_stack_class import CustomStack, StackEmptyException, StackFullException, NumberAscOrder

def test_empty_stack():
    stack = CustomStack(5)
    assert stack.isEmpty() == True
    with pytest.raises(StackEmptyException):
        stack.pop()
    with pytest.raises(StackEmptyException):
        stack.top()

def test_full_stack():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    assert stack.isEmpty() == False
    with pytest.raises(StackFullException):
        stack.push(3)

def test_valid_operations():
    stack = CustomStack(3)
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.size() == 1

def test_element_types():
    stack = CustomStack(3)
    stack.push("string")
    stack.push(123)
    assert stack.pop() == 123
    assert stack.pop() == "string"

def test_max_limit():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    with pytest.raises(StackFullException):
        stack.push(3)

def test_extreme_limits():
    with pytest.raises(StackFullException):
        CustomStack(0)
    CustomStack(10**6)
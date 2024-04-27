import pytest
from custom_stack_class import CustomStack, StackEmptyException, StackFullException, NumberAscOrder

# Atividade I [Melhorada - para ver a primeira versão, verificar o primeiro commit] ✨
@pytest.fixture()
def mock(mocker):
    mock_instance = mocker.MagicMock()
    mocker.patch("custom_stack_class.CustomStack", return_value=mock_instance)
    return mock_instance

def test_empty_stack(mock):
    mock.isEmpty.return_value = True
    mock.pop.side_effect = StackEmptyException
    mock.top.side_effect = StackEmptyException
    
    assert mock.isEmpty() == True
    with pytest.raises(StackEmptyException):
        mock.pop()
    with pytest.raises(StackEmptyException):
        mock.top()


def test_full_stack(mock):
    mock.isEmpty.return_value = False
    mock.push.side_effect = [None, None, StackFullException]

    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)

    assert stack.isEmpty() == False
    with pytest.raises(StackFullException):
        stack.push(3)

def test_valid_operations(mock):
    mock.size.return_value = 2
    mock.top.return_value = 2
    mock.pop.return_value = 2

    assert mock.size() == 2
    assert mock.top() == 2
    assert mock.pop() == 2
    assert mock.size() == 2 

def test_element_types(mock):
    mock.pop.side_effect = [123, "string"]

    stack = CustomStack(3)
    stack.push("string")
    stack.push(123)

    assert stack.pop() == 123
    assert stack.pop() == "string"

def test_max_limit(mock):
    mock.size.return_value = 2
    mock.push.side_effect = [None, None, StackFullException]

    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)

    assert stack.size() == 2
    with pytest.raises(StackFullException):
        stack.push(3)

def test_extreme_limits():
    mock.side_effect = lambda limit: None if limit > 0 else StackFullException

    with pytest.raises(StackFullException):
        CustomStack(0)
    CustomStack(10**6)

def test_negative_limit():
    with pytest.raises(StackFullException):
        CustomStack(-1)

def test_push_when_limit_zero():
    with pytest.raises(StackFullException):
        stack = CustomStack(0)
        stack.push(1)

def test_push_when_limit_one():
    stack = CustomStack(1)
    stack.push(1)
    with pytest.raises(StackFullException):
        stack.push(2)

def test_push_and_top():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.top() == 1

def test_push_and_size():
    stack = CustomStack(3)
    stack.push(1)
    assert stack.size() == 1

def test_sort_with_negative_numbers():
    stack = CustomStack(5)
    stack.push(-3)
    stack.push(0)
    stack.push(5)
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [-3, 0, 5]

def test_sort_with_unsorted_numbers():
    stack = CustomStack(4)
    stack.push(5)
    stack.push(1)
    stack.push(3)
    sorted_numbers = NumberAscOrder.sort(stack)
    assert sorted_numbers == [1, 3, 5]

def test_exception_messages():
    with pytest.raises(StackEmptyException) as exc_info:
        stack = CustomStack(2)
        stack.pop()
    assert str(exc_info.value) == "Stack está vazio."

    with pytest.raises(StackFullException) as exc_info:
        stack = CustomStack(1)
        stack.push(1)
        stack.push(2)
    assert str(exc_info.value) == "Stack está cheio."

def test_top_on_empty_stack():
    stack = CustomStack(3)
    with pytest.raises(StackEmptyException):
        stack.top()

def test_negative_limit_initialization():
    with pytest.raises(StackFullException):
        CustomStack(-1)

# Atividade II ✨
# mockup data
@pytest.fixture()
def full_custom_stack():
    stack = CustomStack(6)
    for number in [15, 9, 2, 27, 42, 59]:
        stack.push(number)
    return stack

@pytest.fixture()
def empty_custom_stack():
    return CustomStack(6)

# tests
def test_sort_with_full_stack(full_custom_stack):
    sorted_numbers = NumberAscOrder.sort(full_custom_stack)
    assert sorted_numbers == [2, 9, 15, 27, 42, 59]

def test_sort_with_empty_stack(empty_custom_stack):
    sorted_numbers = NumberAscOrder.sort(empty_custom_stack)
    assert sorted_numbers == []
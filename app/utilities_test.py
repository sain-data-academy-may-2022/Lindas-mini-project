import utilities
from unittest.mock import Mock, call, patch


# Test print_list function

@patch('builtins.print')
def test_print_list_with_no_items(mock_print: Mock):
    utilities.print_list([])
    mock_print.assert_has_calls([
        call(''), 
        call('No Items!')
    ])

@patch('builtins.print')
def test_print_list_with_items(mock_print: Mock):
    utilities.print_list(['banana', 'lemon'])
    mock_print.assert_has_calls([
        call(''), 
        call('[1] - banana'),
        call('[2] - lemon')
    ])


#  Test get_choice function

@patch('builtins.input', side_effect = ['3'])
def test_get_choice(mock_input: Mock):
    value = utilities.get_choice(['banana', 'apple', 'cherry'])
    assert value == 'cherry'

@patch('builtins.input', side_effect = [''])
def test_get_choice_with_blank(mock_input: Mock):
    # Assemble
    my_list = ['banana', 'apple', 'cherry']
    allow_blank = True
    expected = None
    # Act
    value = utilities.get_choice(my_list, allow_blank)
    # Assert
    assert value == expected

@patch('utilities.print_list')
@patch('builtins.input', side_effect = ['3'])
def test_get_choice_calls_print_list(mock_input: Mock, mock_print_list: Mock):
    utilities.get_choice(['banana', 'apple', 'cherry'])
    mock_print_list.assert_called_with(['banana', 'apple', 'cherry'])
    
@patch('builtins.print')
@patch('builtins.input', side_effect = ['-1', '3'])
def test_get_choice_with_negative_number(mock_input: Mock, mock_print: Mock):
    utilities.get_choice(['Apple', 'Banana', 'Carrot'])
    # This only checks the last time that print was called (ignores calls from print_list!)
    mock_print.assert_called_with('Please select a valid number')

@patch('builtins.print')
@patch('builtins.input', side_effect = ['4', '3'])
def test_get_choice_with_lenght_of_list(mock_input: Mock, mock_print: Mock):
    utilities.get_choice(['Apple', 'Banana', 'Carrot'])
    # This only checks the last time that print was called (ignores calls from print_list!)
    mock_print.assert_called_with('Please select a valid number')

@patch('builtins.print')
@patch('builtins.input', side_effect = ['banana', '3'])
def test_get_choice_with_banana(mock_input: Mock, mock_print: Mock):
    utilities.get_choice(['Apple', 'Banana', 'Carrot'])
    # This only checks the last time that print was called (ignores calls from print_list!)
    mock_print.assert_called_with('Please write a number')


#  Test get_positive_float function

@patch('builtins.input', side_effect = ['0.1'])
def test_get_positive_float(mock_input: Mock):
    value = utilities.get_positive_float('Give me a number')
    assert value == 0.1

@patch('builtins.input', side_effect = ['5.4'])
def test_get_positive_float_with_message(mock_input: Mock):
    message = 'Give me a number'
    utilities.get_positive_float(message)
    mock_input.assert_called_once_with(message)

@patch('builtins.print')
@patch('builtins.input', side_effect = ['0', '0.1'])
def test_get_positive_float_with_negative_int(mock_input: Mock, mock_print: Mock):
    utilities.get_positive_float('Give me a number')
    mock_print.assert_called_once_with('Please select a positive number')

@patch('builtins.print')
@patch('builtins.input', side_effect = ['banana', '5.3'])
def test_get_positive_float_with_banana(mock_input: Mock, mock_print: Mock):
    utilities.get_positive_float('Give me a number')
    mock_print.assert_called_once_with('Please write a number')


# Test get_positive_int function

@patch('builtins.input', side_effect = ['5'])
def test_get_positive_int(mock_input: Mock):
    value = utilities.get_positive_int_or_zero('Give me a number')
    assert value == 5

@patch('builtins.input', side_effect = ['5'])
def test_get_positive_int_with_message(mock_input: Mock):
    message = 'Give me a number'
    utilities.get_positive_int_or_zero(message)
    mock_input.assert_called_once_with(message)

@patch('builtins.print')
@patch('builtins.input', side_effect = ['-1', '0'])
def test_get_positive_int_with_negative_int(mock_input: Mock, mock_print: Mock):
    utilities.get_positive_int_or_zero('Give me a number')
    mock_print.assert_called_once_with('Please select a positive number')

@patch('builtins.print')
@patch('builtins.input', side_effect = ['banana', '5'])
def test_get_positive_int_with_banana(mock_input: Mock, mock_print: Mock):
    utilities.get_positive_int_or_zero('Give me a number')
    mock_print.assert_called_once_with('Please write a number')

def test_dict_without():
    input = {'wib': 1, 'rar': 'Woo', 'Three': 'Yep'}
    actual = utilities.dict_without(input, ['rar', 'blah'])
    assert actual == {'wib': 1, 'Three': 'Yep'}

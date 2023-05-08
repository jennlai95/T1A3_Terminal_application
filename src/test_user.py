import pytest
from user import get_user

test_user_file = "tests/test_user.csv"

def test_get_user(monkeypatch):
    input_values = ['John', 'john@gmail.com', '123']
    expected_output = {'name': 'John', 'email': 'john@gmail.com', 'phone': 123}

    # Simulate user input
    def mock_input(prompt):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the function and capture the returned value
    result = get_user()

    # Check the returned value against the expected output
    assert result == expected_output

  
from main import create_menu
from unittest import mock

def test_create_menu(capsys):
    expected_output = (
        "Enter 1 to add your user information\n"
        "Enter 2 to view available rooms\n"
        "Enter 3 to make a new booking\n"
        "Enter 4 to view past booking\n"
        "Enter 5 to exit\n"
    )
    with mock.patch('builtins.input', return_value='5'):
        assert create_menu() == '5'
    captured = capsys.readouterr()
    assert captured.out == expected_output
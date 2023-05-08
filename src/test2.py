import pytest 
import csv 
# doing testing for bookings.py
@pytest.fixture
def sample_csv():
    data = [
        ["Apple", "A","100", "3"],
        ["Bob", "B","150", "4"],
        ["Cat", "C","200", "5"],
        ["Dog", "D","250", "6"]
    ]
from booking import display_bookings
# assertion
def test_display_bookings():
    excpected_output = 
    assert excpected_output == capture_output
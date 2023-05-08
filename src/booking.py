from user import get_user
import csv 
import datetime

# defined booking files
BOOKING_FILES = "bookings.csv"

# defined display bookings menu
def display_bookings():
    with open("bookings.csv", mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            print("User:", row[0])
            print("Room Choice:", row[1])
            print("Total Cost:", row[2])
            print("Number of Nights:", row[3])
            print("Booking date:", row[4])
            print("----------------------------")
 

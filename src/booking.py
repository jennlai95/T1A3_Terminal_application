# today = date.today ()
    
# def new_booking():
#     print (today) 
#     print("total number of days")
#     choose
#     add (new_booking)


# # User info and login
# def get_user(self):
#     self.name = input("Enter your name: ")
#     self.email = input("Enter your email:")
#     self.phone = input("Enter your phone number here: ")
#     return {"name": self.name, "email": self.email, "phone" : self.phone}

import csv 
from hotel_room import room_choice_menu, room_type, room_choice

BOOKING_FILES = "booking.csv"

def add_booking(booking):
    with open(BOOKING_FILES,"a",) as f:
        writer = csv.writer(f)
        writer.writerow(booking["user_info"]["name"]),
        booking["user_info"]["email"],
        booking["room_info"]["room_choice"]



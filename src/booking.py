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


BOOKING_FILES = "bookings.csv"

def display_bookings():
    with open("bookings.csv", mode="r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader) 
        for row in reader:
            print("User:", row[0])
            print("Room Choice:", row[1])
            print("Total Cost:", row[2])
            print("Number of Nights:", row[3])
            print("----------------------------")
            

# def add_booking(booking):
#     with open(BOOKING_FILES,"a",) as f:
#         writer = csv.writer(f)
#         writer.writerow(booking["user_info"]["name"]),
#         booking["user_info"]["email"],
#         booking["room_info"]["room_choice"],



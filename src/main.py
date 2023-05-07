# import modules & packages
import csv
import style
from colored import fg,bg, attr
import datetime
from hotel_room import room_choice_menu, room_type
from user import get_user
from booking import display_bookings

# Welcome message
print(f"{fg('blue')} {bg('yellow')}Welcome to Hotel booking {attr('reset')}")

# making a booking 
current_booking = "booking_records.csv"
user_info = get_user
room_choice = room_choice_menu
booking = {"user_info": user_info, "room_choice": room_choice}


# main menu 
def create_menu():
    print("Enter 1 to add your user information")
    print("Enter 2 to view available rooms")
    print("Enter 3 to make a new booking")
    print("Enter 4 to view past booking")
    print("Enter 5 to exit")
    choice = input("Enter your selection:")
    return choice

user_choice = ""
print(user_choice)
file_name = "bookings.csv"

# main menu loop and choices
while user_choice != "5":
    user_choice = create_menu()
    
    if (user_choice == "1"):
        print(user_info())
    elif (user_choice == "2"):
        print(room_type)
        user_input = input(style.bold('Would you like to make a new booking Y or N?: '))
        if user_input == 'Y':
            user_choice == "3"
        elif user_input == 'N':
            print (style.bold("Thank you for browsing! We will take you back to the main menu"))
            continue
        else: 
            print(f"{fg('red')}Invalid input, returning to main menu{attr('reset')}")
    elif (user_choice == "3"):
        try:
            result= room_choice_menu()
            confirmation = input("Please confirm if you would like to make this booking? Yes or No: ")
            if confirmation == "Yes":
                    print(style.bold("Thank you for booking with us"))         
            elif confirmation == "No":
                pass
            elif user_input == 'N':
                print (style.italic("Thank you for browsing! We will take you back to the main menu"))
                continue
        except Exception as e:
            print("An error occurred: ", e)
    elif (user_choice == "4"):
        print("Previous booking records")
        # check if bookings.csv exists
        try:
            display_bookings()
        # if it exists then all is fine
        except FileNotFoundError as e:
            booking_file = open(file_name,"w")
            booking_file.write ("Booking records")
            booking_file.close()
            print ("In except block")           
    elif (user_choice == "5"):
        continue
    else: 
       print(f"{fg('red')}Invalid input{attr('reset')}")
       
    input("press enter to continue....")


print(style.bold (style.italic("Thank you for using the Hotel booking app")))

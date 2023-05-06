import datetime
import csv
from user import get_user

# class Room:
#     def _init_(self,room_type,price,capacity):
#         self.type = room_type
#         self.price = price
#         self.capacity = capacity
#         print(self)
    
 #room_type list  
room_type = [('single: $100/night'), ('double: $150/night'), ('twin:$200/night'),('queen:$300/night')]


def room_choice_menu():
    print ("Here are the available rooms! Press enter to continue")
    print("The list of available rooms:")
    print("A. Single room: $100/night")
    print("B. Double room: $150/night")
    print("C. Twin room: $200/night")
    print("D. Queen: $300/night")
    print("E to Exit to menu")

   
    while True:
        try:
            n = int(input("Please choose the length of your stay: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Please input a positive integer or input 0 if you want to exit")
   

    room_choice = input("Please enter the letter of the room of your choice: ")
       
    if room_choice == "A":
        room_price = 100
        print("Single room chosen at $100 per night")
    elif room_choice == "B":
        room_price = 150
        print("Double room chosen at $150 per night")
    elif room_choice == "C":
        room_price = 200
        print("Twin room chosen at $200 per night")
    elif room_choice == "D":
        room_price = 300
        print("Queen room chosen at $300 per night")
    elif room_choice == "E":
        exit ()
    else:
        print("Invalid room choice, please enter the Letter A, B, C or D for your choices")
        room_price = 0
    
    
    total_cost = n * room_price
    print(f"Total cost for {n} nights: ${total_cost}")

    with open("bookings.csv", mode="a", newline="") as csvfile:
         writer = csv.writer(csvfile)
         #  Recording the booking to CSV
         writer.writerow([get_user(),room_choice,total_cost,n])
    return room_choice, total_cost,n 
     

# # Get user's room choice
# room_choice = room_choice_menu()


 
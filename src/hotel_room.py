import datetime
import csv
import style
from colored import fg,bg,attr
from user import get_user  

# class Room:
#     def _init_(self,room_type,price,capacity):
#         self.type = room_type
#         self.price = price
#         self.capacity = capacity
#         print(self)
    
 #define room_type list  
room_type = [('A. Single room: $100/night'), ('B. Double: $150/night'), ('C. Twin:$200/night'),('D. Queen:$300/night')]

# Get the current date
current_date = datetime.datetime.now().strftime("%Y-%m-%d")

# menu to for user to choose a room and book
def room_choice_menu():
    print ("Here are the available rooms!")
    print("A. Single room: $100/night")
    print("B. Double room: $150/night")
    print("C. Twin room: $200/night")
    print("D. Queen: $300/night")
    print("E to Exit program")

#    prompts user to input length of stay to calculate the total price
    while True:
        try:
            n = int(input("Please choose the length of your stay: "))
            if n == 0:
                print ("returning to main menu")
                
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print(f"{fg('red')}Please input a positive integer or input 0 if you want to exit{attr('reset')}")
   
# prompts user to choose a room and error handling
    while True:
        try:
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
                print(style.bold (style.italic("Thank you for using the Hotel booking app")))
                exit ()
            else:
                raise ValueError
            break
        except ValueError:
            print(f"{fg('red')}Invalid room choice, please enter the Letter A, B, C or D for your choices{attr('reset')}")
            room_price = 0
    
        # calculate total cost and records the room booking to CSV
        total_cost = n * room_price
        print(current_date)
        print(style.bold(f"Total cost for {n} nights: ${total_cost}"))

        with open("bookings.csv", mode="a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            #  Recording the booking to CSV
            writer.writerow([get_user(),room_choice,total_cost,n,current_date])
        return room_choice, total_cost,n,current_date
        


 
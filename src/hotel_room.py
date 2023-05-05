import datetime
class Room:
    def _init_(self,room_type,price,capacity):
        self.type = room_type
        self.price = price
        self.capacity = capacity
        print(self)
    
 #room_type list  
room_type = [('single: $100'), ('double: $150'), ('twin:$200'),('queen:$300')]

def room_choice_menu():
    print ("Here are the available rooms! Press enter to continue")
    print("The list of available rooms:")
    print("A. Single room: $100/night")
    print("B. Double room: $150/night")
    print("C. Twin room: $200/night")
    print("D. Queen: $300/night")
   

    room_choice = input("Please enter the room number of your choice: ")
    room_choice = ""
    n = int(input("Please choose the length of your stay: "))
    
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
    else:
        print("Invalid room choice")
        room_price = 0

    total_cost = n * room_price
    print(f"Total cost for {n} nights: ${total_cost}")
    return room_choice


import datetime
class Room:
    def _init_(self,room_type,price,capacity):
        self.type = room_type
        self.price = price
        self.capacity = capacity
        print(self)
    
 #room_type list  
room_type = [('single: $100'), ('double: $150'), ('twin:$200'),('queen:$300')]


print ("Here are the available rooms! Press enter to continue")

def room_choice_menu(n):
    print("The list of available rooms:")
    print("1. Single room: $100/night")
    print("2. Double room: $150/night")
    print("3. Twin room: $200/night")
    print("4. Queen: $300/night")
   

    room_choice = input("Please enter the room number of your choice: ")

    if room_choice == "1":
        room_price = 100
        print("Single room chosen at $100 per night")
    elif room_choice == "2":
        room_price = 150
        print("Double room chosen at $150 per night")
    elif room_choice == "3":
        room_price = 200
        print("Twin room chosen at $200 per night")
    elif room_choice == "4":
        room_price = 300
        print("Queen room chosen at $300 per night")
    else:
        print("Invalid room choice")
        room_price = 0

    total_cost = n * room_price
    print(f"Total cost for {n} nights: ${total_cost}")
    return room_choice

room_choice = ""
n = int(input("Please choose the length of your stay: "))
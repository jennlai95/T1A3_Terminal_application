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
    print ("The list of avaiable rooms:")
    print ("1.single room: $100/night")
    print ("2 double room: $150/night")
    print ("twin room :$200/night")
    print ("queen:$300/night")
    room_choice = input("Please enter the room number of your choice")
    n= int(input("Please choose the length of your stay"))
           
    if (room_choice == "1"):
        print ("Single room chosen at $100 per night")
        self.price =100*n 
        
 
price = self.price

print ("Here are the available rooms!")

def room_choice_menu(self):
    print ("The list of avaiable rooms:")
    print ("1.single room: $100/night")
    print ("2 double room: $150/night")
    print ("3. twin room :$200/night")
    print ("4. queen:$300/night")
    print ("5. Go back to original menu")
    room_choice = input("Please enter the room number of your choice")
    n = int(input("Please choose the length of your stay: "))
    return room_choice

room_choice = ""
print (room_choice)

while room_choice != "5"
    room_choice = room_choice_menu()
    
    if (room_choice == "1"):
        print ("Single room chosen at $100 per night")
        self.price =100*n 

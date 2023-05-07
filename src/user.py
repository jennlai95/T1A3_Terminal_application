import csv 

# User info and login
def get_user():
    name = input("Enter your name: ")
    email = input("Enter your email:")
    while True: 
        try:
            phone = int(input("Enter your phone number here: "))
            break
        except ValueError:
            print("Invalid input. Please enter phone number")
    user_data = {"name": name, "email": email, "phone" : phone}
    with open ('user_data.csv', mode= 'a') as csv_file:
            fieldnames = ['name','email','phone']
            writer =  csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(user_data)
    # phone = input("Enter your phone number here: ")

    print(user_data)
get_user
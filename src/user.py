# User info and login
def get_user():
    name = input("Enter your name: ")
    email = input("Enter your email:")
    phone = input("Enter your phone number here: ")
    return {"name": name, "email": email, "phone" : phone}
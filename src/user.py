# User info and login
def get_user(self):
    self.name = input("Enter your name: ")
    self.email = input("Enter your email:")
    self.phone = input("Enter your phone number here: ")
    return {"name": self.name, "email": self.email, "phone" : self.phone}
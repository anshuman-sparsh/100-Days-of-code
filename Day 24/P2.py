# 🔹 2. User → Admin Inheritance
# Create a User class with name and method display_info().
# Extend it with Admin, which adds permissions and overrides display.



class User:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"User Name: {self.name}")

class Admin(User):
    def __init__(self, name, permissions):
        super().__init__(name)
        self.permissions = permissions

    def display_info(self):
        print(f"Admin Name: {self.name}")
        print(f"Permissions: {', '.join(self.permissions)}")

u = User("anshuman_62")
a = Admin("Anshuman", ["add_user", "delete_user", "view_reports"])

u.display_info()
a.display_info()
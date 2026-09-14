# 
admin_username ="admin"
admin_password = 1212
import time
def greet():
    print("========Water Refilling Transaction and Reciept system========")


def Costumer_interface():
    Choices = ["1. check water refilling", "2. check reciept", "3. Exit"]
    print(*Choices, sep="\n")
    
    while true:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                print("Checking Water refilling....")
                time.sleep(1)
                return Costumer_interface()
                
            


def admin_interface():
    print("========Admin Interface========")
    Achoices = ["1. check water refilling", "2. check reciept", "3. Add water refilling", "4. Add reciept", "5. Exit"]
    print(*Achoices, sep="\n")
    
    while True:
        if choice == 1:
            print("Checking Water refilling....")
            time.sleep(1)


def costumer_choices():
    print("========Customer Choices========")
    Cchoices = ["1. log in", "2. Register", "3. Exit"]
    print(*Cchoices, sep="\n")
    choice = int(input("Enter your choice: "))
    
    while True:
        if choice == 1:
            customer_login()
            break
        elif choice == 2:
            print("Registering...")
            time.sleep(1)
            return costumer_choices()
        elif choice == 3:
            print("Exiting...")
            time.sleep(1)
            return main_menu()
        else:
            print("Invalid choice. Please try again.")
            return costumer_choices()

def login_admin():
    print("========Login admin========")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == admin_username and password == admin_password:
        print(f"Welcome, {username}!")
    else:
        print("invalid username or password. Please try again.")
        return login_admin()






def customer_login():
    print("========Customer log in========")
    username1 = input("Enter your username: ")
    password1 = input("Enter your password: ")
    if username1 == admin_username and password1 == admin_password:
        print(f"Welcome, {username1}!")
    else:
        print("invalid username or password. Please try again.")
        return customer_login()
    # Add customer functionality here


def register_customer():
    print("========Customer Registration========")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    while True:
        if username == admin_username:
            print("Username already exists. Please try again.")
            return register_customer()
        else:
            print(f"Customer {username} registered successfully!")
            break


def main_menu():
    time.sleep(0.5)
    options = ["1. Admin", "2. Customer", "3. Exit"]
    print(*options, sep="\n")
    
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                login_admin()
                break
            elif choice == 2:
                customer_login()
                break
            elif choice == 3:
                print("Exiting...")
                time.sleep(1)
                return main_menu()
                
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
greet()
main_menu()


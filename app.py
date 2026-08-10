import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxy"
numbers = "0123456789"
symbols = "@$#!-_"

print("Welcome to PassGen!")

exit_loop = False
while not exit_loop:
    try:
        length = int(input("Password length (10-25): "))
        if length < 10 or length > 25:
            print("ERROR: Length must be between 10 and 25")
        else:
            password = "".join(random.choices(upper + lower + numbers + symbols, k=length))
            print(password)
            if input("Enter 'x' to exit the program: ") == "x":
                exit_loop = True
    except:
        print("ERROR: Length must be between 10 and 25")
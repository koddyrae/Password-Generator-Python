import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print_times = 0

while print_times != 1:
    password_len = int(input ("How long would you like your password to be: "))
    password_count = int(input("How many passwords would you like: "))

    for x in range(0,password_count): 
        password = ""
        for x in range (0, password_len):
            password_char = random.choice(chars)
            password += password_char
        print("The generated password: ", password)
    print_times = 1

def main():
    password = input("Enter password of 8 characters minimum: ")
    while len(password) < 8:
        print("Password must have at least 8 characters inclusive")
        password = input("Enter password of 8 characters minimum: ")
    for a in password:
        print("*", end="")


main()
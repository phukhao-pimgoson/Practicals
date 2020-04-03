def main():
    password = get_password()
    censor_password(password)


def censor_password(password):
    for a in password:
        print("*", end="")


def get_password():
    password = input("Enter password of 8 characters minimum: ")
    while len(password) < 8:
        print("Password must have at least 8 characters inclusive")
        password = input("Enter password of 8 characters minimum: ")
    return password


main()
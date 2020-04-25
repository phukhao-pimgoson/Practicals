def main():
    email_name = {}
    email = valid("Enter email here: ")
    while email != "":
        name = get_name(email)
        confirm = input("Is your name {}? (Y/n) ".format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_name[email] = name
        email = input("Email: ")
    for email, name in email_name.items():
        print("{} ({})".format(name, email))


def valid(prompt):  # validates input as a valid email
    string = input(prompt)
    while not (("@" in string) and ("." in string)):
        print("Please enter a valid email")
        string = input(prompt)
    return string


def get_name(email):
    full_name = email.split("@")[0]
    split_name = full_name.split(".")
    name = " ".join(split_name).title()
    return name


main()

from Practical6.guitar_class import Guitar


def main():
    guitars = []
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My Guitars!")
    name = input("Name: ")
    while len(name.split()) != 0:
        year = num_check("Year: ")
        cost = num_check("Cost: ")
        print("{:>20} ({}) : ${:10,.2f}".format(name, year, cost))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")
    print("... Snip ...")
    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))


def num_check(prompt):  # number check validation; input must be 0 or higher
    number = type_check(prompt)
    while number < 0:
        print("Number must be >= 0")
        number = type_check(prompt)
    return number


def type_check(prompt):  # type check validation
    user_input = ""
    while user_input == "":
        try:
            user_input = int(presence_check(prompt))
        except ValueError:
            print("Invalid Input; enter a valid number")
            user_input = ""
    return user_input


def presence_check(prompt):  # presence check validation
    user_input = input(prompt)
    while len(user_input.split()) == 0:
        print("Input can not be blank")
        user_input = input(prompt)
    return user_input


main()

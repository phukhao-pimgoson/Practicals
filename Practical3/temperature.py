def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(cel_to_fah(celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(fah_to_cel(fahrenheit))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def fah_to_cel(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return "Result: {:.2f} C".format(celsius)


def cel_to_fah(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return "Result: {:.2f} F".format(fahrenheit)


main()
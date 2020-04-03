"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    print("Welcome to Bonus Calculator")
    print("Enter Sales value below. Enter a(ny) negative value to quit")
    sales = float(input("Input> $"))
    while sales > 0:
        if sales >= 1000:
            bonus = sales * 0.15
        elif sales >= 0:
            bonus = sales * 0.1
        else:
            bonus = 0
            print("[ERROR]")
            quit()
        print("Your bonus is ${:.2f}".format(bonus))
        print("Enter Sales value below. Enter a(ny) negative value to quit")
        sales = float(input("Input> $"))
    print("Thank you")


if __name__ == "__main__":
    main()

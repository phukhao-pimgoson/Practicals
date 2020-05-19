"""Function to test the silver service taxis"""

from Practical8.silverservicetaxi import SilverService


def main():
    taxi = SilverService("Mercedes S500L", 100, 2)
    taxi.drive(18)
    print(taxi)
    print("${:.2f}".format(taxi.get_fare()))


main()

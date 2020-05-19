from Practical8.unreliable_car import Unreliable


def main():
    reliable = Unreliable("Mostly Good", 100, 90)
    unreliable = Unreliable("Dodgy", 100, 9)
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(reliable.name, reliable.drive(i)))
        print("{:12} drove {:2}km".format(unreliable.name, unreliable.drive(i)))
    print(reliable)
    print(unreliable)


if __name__ == '__main__':
    main()

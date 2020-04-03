import time


def main():
    number = 0
    print("Let's get loopy!")
    for i in range(1, 21, 2):
        print(i, end=' ')
        time.sleep(0.1)
    print()
    time.sleep(1)
    for i in range(0, 101, 10):
        print(i, end=' ')
        time.sleep(0.1)
    print()
    time.sleep(1)
    for i in range(20, -1, -1):
        print(i, end=' ')
        time.sleep(0.1)
    print()
    time.sleep(1)
    print("Time of your input!")
    stars = int(input("Enter number of Stars: "))
    while stars > 0:
        number += 1
        for i in range(0, number, 1):
            print("*", end='')
        print()
        stars -= 1


if __name__ == "__main__":
    main()
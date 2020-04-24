def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(numbers[0])  # 3
    print(numbers[-1])  # 2?
    print(numbers[3])  # 1
    print(numbers[:-1])  # what
    print(numbers[3:4])  # 1
    print(5 in numbers)  # Yes
    print(7 in numbers)  # No
    print("3" in numbers)  # No
    print(numbers + [6, 5, 3])  # appending

    numbers[0] = "ten"
    numbers[-1] = 1
    print(numbers[2:])  # the previous append was exclusive to the print statement
    print(9 in numbers)


main()

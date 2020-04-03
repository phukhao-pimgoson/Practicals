def validation_check(prompt):
    num = float(input(prompt))
    while num < 0:
        print("Please enter a positive value")
        num = float(input(prompt))
    return num


def main():
    cost = 0
    item = int(validation_check("Number of items: "))
    for i in range(item):
        cost += float(validation_check("Price of item #"+str(i+1)+": $"))
    print("Total price for "+str(item)+" items is ${:.2f}".format(cost))


if __name__ == "__main__":
    main()
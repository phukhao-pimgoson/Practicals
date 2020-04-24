def main():
    numbers = []
    for counter in range(5):
        numbers.append(int(input("Enter number {}: ".format(counter + 1))))
    print("The 1st number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The biggest number is {}".format(max(numbers)))
    print("The average of the numbers is {:.2}".format(sum(numbers) / len(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    if input("Enter username") in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()

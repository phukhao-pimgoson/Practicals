name_file = open("name.txt", "w")
print(input("What is your name?"), file=name_file)
name_file.close()
read_name = open("name.txt", "r")
print("Your name is "+read_name.read())
read_name.close()

numbers_file = open("numbers.txt", "r")
num1 = int(numbers_file.readline())
num2 = int(numbers_file.readline())
print(num1 + num2)
numbers_file.close()

numbers_list = open("numbers.txt", "r")
listing = numbers_list.readlines()
total = 0
for counter in range(len(listing)):
    total += int(list[counter])
print(total)




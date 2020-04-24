import random
NUM_PER_LINE = 6
MIN_NUM = 1
MAX_NUM = 45

for lines in range(int(input("How many quick picks? "))):
    list = []
    for numbers in range(NUM_PER_LINE):
        value = random.randint(MIN_NUM,MAX_NUM)
        while value in list:
            value = random.randint(MIN_NUM, MAX_NUM)
        list.append(value)
    list.sort()
    print(" ".join("{:2}".format(number) for number in list))
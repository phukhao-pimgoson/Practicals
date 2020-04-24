import random
NUM_PER_LINE = 6
MIN_NUM = 1
MAX_NUM = 45


def main():
    for lines in range(int(input("How many quick picks? "))):
        picks = []
        for numbers in range(NUM_PER_LINE):
            value = random.randint(MIN_NUM, MAX_NUM)
            while value in picks:
                value = random.randint(MIN_NUM, MAX_NUM)
            picks.append(value)
        picks.sort()
        print(" ".join("{:2}".format(number) for number in picks))


main()

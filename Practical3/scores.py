import random


def main():
    count = int(input("How many scores to generate? >>>"))
    for a in range(count):
        points = random.randint(0, 100)
        print(str(points)+" is "+grading(points))


def grading(score):
    if (score > 100) or (score < 0):
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
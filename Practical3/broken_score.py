"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(grading(score))
    score = random.randint(0, 100)
    print("random score: "+str(score)+"; grade: "+grading(score))


def grading(score):
    if (score > 100) or (score < 0):
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()

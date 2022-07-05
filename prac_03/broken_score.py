"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""



import random

def main():
    score = random_score()
    result = calculation_grade(score)
    print("Your grade is {} and your grade is {}".format(score, result))


def calculation_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def random_score():
    return random.randint(1,101)

main()




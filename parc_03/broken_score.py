"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status
"""

# Check your boundary conditions (e.g. >= 50 should be a pass, not just > 50)
# Think about efficiency and nesting; use the fewest number of if/elif
# "The Zen of Python" says, "Flat is better than nested."
# https://www.python.org/dev/peps/pep-0020/
# Also note that here we only have one path for "Invalid score" (DRY principle)
# You want to make sure the last path is "else", not "elif" as we always want a result here,
# so there should be no final condition (if it wasn't one of the earlier possibilities,
# it must be the last thing, no need to check if it is)

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



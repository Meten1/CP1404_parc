import random

def main():
    OUT_FILE = "result.txt"
    out_file = open(OUT_FILE, "a")
    score = random_score()
    result = calculation_grade(score)
    print("{:<2} is {:1}".format(score, result), file = out_file)
    out_file.close()

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
"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

def main():

    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"

    word_format = str(input("Enter the string format you want (for example, ccvc): ").lower())
    error_check = is_valid_format(word_format)
    while error_check == False:
        print("Inter error")
        word_format = str(input("Enter the string format you want (for example, ccvc): ").lower())
        error_check = is_valid_format(word_format)

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)



def is_valid_format(word_format):
    if word_format == "":
        return False
    for word in word_format:
        if word != "c" and word != "v":
            return False


main()

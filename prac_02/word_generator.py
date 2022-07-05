"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#
# word_format = str(input("Enter the string format you want (for example, ccvc): ").lower())
# word = ""
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     else:
#         word += random.choice(VOWELS)
#
# print(word)

# import random
#
# VOWELS = "aeiou"
# CONSONANTS = "bcdfghjklmnpqrstvwxyz"
#
# word_format = str(input("Enter the string format you want (for example, ccvc): ").lower())
# word = ""
# for kind in word_format:
#     if kind == "c" or kind == "#":
#         word += random.choice(CONSONANTS)
#     elif kind == "v" or kind == "%":
#         word += random.choice(VOWELS)
#     elif kind in VOWELS or kind in CONSONANTS:
#         word += kind
#
# print(word)


import random
def main():
    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"

    word_format = get_word_format()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)

def get_word_format():
    word_lenth = random.randint(1, 10)
    choice_list = "cv"
    word_format = ""
    for word_lenth in range(1, word_lenth):
        one_choice = random.choice(choice_list)
        word_format += one_choice
    return word_format

main()




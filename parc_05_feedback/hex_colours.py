NAME_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}

color_name = str(input("Enter the color name: "))
while color_name != "":
    if color_name in NAME_TO_CODE:
        print("{}'s code is {}".format(color_name, NAME_TO_CODE[color_name]))
    else:
        print("Input error!")
    color_name = str(input("Enter the color name: "))

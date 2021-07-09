import random

# Function - Create an array with all the mayus, minus, nums and chars in the keyboard, and join them into an array
def passwordGenerator():
    MAYUS = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "Ñ",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "X",
        "Y",
        "Z",
    ]
    MINUS = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "ñ",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "x",
        "y",
        "z",
    ]
    NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    CHARS = [
        "*",
        "+",
        "-",
        "/",
        "@",
        "_",
        "?",
        "!",
        "[",
        "{",
        "(",
        ")",
        "}",
        "]",
        ",",
        ";",
        ".",
        ">",
        "<",
        "~",
        "°",
        "^",
        "&",
        "$",
        "#",
        '"',
    ]

    characters = MAYUS + MINUS + NUMS + CHARS

    secret = []

    for i in range(15):
        character_random = random.choice(characters)
        secret.append(character_random)

    secret = "".join(secret)
    return secret

password = passwordGenerator()
print(f"You password is {password}")

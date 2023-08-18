# import os
char_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
             "v", "w", "x", "y", "z", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ",", ".", "?", ";", "-", "“", "=", ":", "/", "‘",
             "$", "+",
             "@", "_"]
morse_code_list = [". _", "_ . . .", "_ . _.", "_ . .", ".", ". . _ .", "_ _ .", ". . . .", ". .", ". _ _ _",
                   "_ . _", ". _ . .", "_ _", "_.", "_ _ _", ". _ _ .", "_ _ . _", ". _ .", ". . .", "_", ". . _",
                   ". . . _", ". _ _", "_ . . _", "_ . _ _", "_ _ . .", ". _", ". . _", ". . . _", ". . . . _", ".",
                   "_ . . . .", "_ . . .", "_ . .", "_ .", "-----", "_ _ . . _ _", ". _ . _. _", ". . _ _ . .",
                   "_ . _ . _ .", "_ . . . . _", ". _ . . _.", "_ . . . _", "_ _ _ . . .", "_ . . _.", ". _ _ _ _.",
                   ". . . _ . . _", ". _ . _.", "·−−·−·", "··−−·−"]

Convert = True


def converter():
    letters = input("Enter any from the list of the following (letter, word, numbers, signs, or sentence), to convert "
                    "to morse code:\n").lower()
    morse_code = ''
    for letter in letters:
        if letter in char_list:
            char_index = char_list.index(letter)
            morse_code += morse_code_list[char_index]
        elif letter not in char_list and letter == " ":
            morse_code += "/"
        else:
            morse_code += letter

    print(f"Here is the code: {morse_code}")


converter()
while Convert:
    another_one = input("Type Yes to do another conversion or No to exit:\n").lower()
    if another_one == "yes":
        # os.system('cls' if os.name == 'nt' else 'clear')
        converter()
    else:
        Convert = False
        print("Goodbye")

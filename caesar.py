def alphabet_position(letter):
    if letter.isupper():
        alpha_num = ord(letter) - 65
    elif letter.islower():
        alpha_num = ord(letter) - 97
    return alpha_num

def rotate_character(char, rot):
#Lists of letters to hande upper an dlower
    a_lower = 'abcdefghijklmnopqrstuvwxyz'
    a_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rot = int(rot)
#If it's a space do nothing except pass it through
    if char is "" == False:
        return ""
#If it's not a letter then skip and return char
    elif char.isalpha() == False:
        return char
#If lowercase letter then handle this way
    elif char in a_lower:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
             return a_lower[rotated_index]
        else:
            return a_lower[rotated_index % 26]
#If uppercase letter then handle this way
    elif char in a_upper:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
             return a_upper[rotated_index]
        else:
            return a_upper[rotated_index % 26]

def encrypt(text,rot):
    caesar_text = ""
    for char in text:
        caesar_text += rotate_character(char, rot)
    return caesar_text

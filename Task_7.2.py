def code_cesar(letter, shift):
    if letter.isalpha():
        number = ord(letter) + shift % 26
        if number > 122:
            number -= 26
        return chr(number)
    return letter


shift = int(input())
for i in input():
    print(code_cesar(i, shift), end='')
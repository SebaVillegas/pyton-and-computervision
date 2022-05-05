from art import logo

abecedario = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g",
              8: "h", 9: "i", 10: "j", 11: "k", 12: "l", 13: "m",
              14: "n", 15: "o", 16: "p", 17: "q", 18: "r", 19: "s",
              20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z"}

print(logo)


def caesar(text, shift, mode):
    cipher = []
    shift = shift % 26
    index = 0

    for i in range(len(text)):
        if text[i] in abecedario.values():
            for j in range(1, len(abecedario)+1):
                if text[i] == abecedario[j]:
                    if mode == "encode":
                        index = j + shift
                        if index > 26:
                            index -= 26
                        elif index < 1:
                            index += 26
                    else:
                        index = j - shift
                        if index < 1:
                            index += 26
                        elif index > 26:
                            index -= 26
                    cipher.append(abecedario[index])
        else:
            cipher.append(text[i])

    cipher = "".join(cipher)
    return cipher


sel = "1"

while sel == "1":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    while direction != "encode" and direction != "decode":
        direction = input("pls, select \'encode\' or \'decode\': ")

    if direction == "encode":
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        result = caesar(text, shift, direction)
        print(f"The message encode is: {result}\n")
        sel = input("select 1 if you want to repeat or 0 for exit: ")
    elif direction == "decode":
        text = input("Type your message: ").lower()
        shift = int(input("Type the shift number: "))
        result = caesar(text, shift, direction)
        print(f"The message encode is: {result}\n")
        sel = input("select 1 if you want to repeat or 0 for exit: ")

    while sel != "1" and sel != "0":
        sel = input("select 1 if you want to repeat or 0 for exit: ")

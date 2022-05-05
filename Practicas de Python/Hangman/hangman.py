import random
import ascii_hangman as art

print(art.logo)

word_list = ["calendario", "musica", "pochoclo", "beto", "corazon", "animal", "veterinaria", 
             "canivalismo", "mariposa", "clinica", "otorrinolaringologo", "edificacion", "metropolitano", 
             "rosquilla", "celular", "ascensor", "crucigrama", "manipulacion", "estructura"]

chosen_word = random.choice(word_list)
display = []
index = 6

for i in chosen_word:
    display.append("_")

while "_" in display:
    print(art.stages[index])
    print("\n")
    print(" ".join(display))
    print("\n")
    
    guess = input("Intente adivinar una letra o la palabra: ").lower()
    while len(guess) > 1 and guess != chosen_word:
        guess = input("Ingrese solo una letra o la palabra correcta: ")
    
    if guess == chosen_word:
        print("\n")
        print("GANASTE LOCO BIEN AHI\n")
        break
    
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
    else:
        index = index - 1
        if index == 0:
            print(art.stages[index])
            print(f"La palabra era: {chosen_word}")
            print("YOU LOOSE, TODO MAL\n")
            break
else:
    print("".join(display))
    print("\n")
    print("YOU WON, BIEN AHI\n")


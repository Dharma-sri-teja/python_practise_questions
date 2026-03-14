import random
word_list= ["apple", "banana", "orange", "mango", "pineapple"]
lives=6

choosen_word = random.choice(word_list)
print(choosen_word)
display=[]
for i in range(len(choosen_word)):
    display.append("_")
print(display)
game_over = False
while not game_over:
    guessed_letters = input("Guess letters: ") #b
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guessed_letters:
            display[position] = guessed_letters
            print(display)
        if guessed_letters not in choosen_word:
            lives-=1
            if lives == 0:
                game_over = True
                print("You Lose!")
        if "_" not in display:
            game_over = True
            print("You Win!")

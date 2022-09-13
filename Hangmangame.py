
import random
from hangman_words import word_list 

word_list = ['Horse', 'Mouse', 'Backwood', 'camel', 'baboon']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

from Hangman_art import stages, logo
print(logo)

print(f"Hello, the solution is {chosen_word}. ")

#Creating an empty list and calling it display, for each letter in the chosen_word, add "_" to display
display = []
for _ in range(word_length):
    display += "_"

#Ask the user to guess a letter and assign it to a variable called guess

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    #Checking if the letter the user guessed is one of the letters in the chosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
#Checking if the user has got all letter
    if "_" not in display:
        end_of_game = True
        print("You win.")
#Checking if guess is not a letter in the chosen_word, if life goes down to 0, game ends and prints("You lose!")
    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life" )
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
    
    print(stages[lives])
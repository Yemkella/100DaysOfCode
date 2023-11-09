import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

end_of_game = False
lives = 6

print(logo)
print("How many players are playing hangman?")
player_count = input("1 or 2: ")

if player_count == "1":
  chosen_word = random.choice(word_list)
elif player_count == "2":
  chosen_word = input("Player 1: Type a word for player 2 to guess. \n").lower()
  print("Ok player 2: Start guessing! ")
else:
  print("Sorry, that's not the answer we were looking for. Only 1 or 2 please! ")

word_length = len(chosen_word)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
  
#Give the user a hint of how many letters the word is
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've already guessed {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong and let them know if the letter isn't in the word and if they lost.
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the word. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
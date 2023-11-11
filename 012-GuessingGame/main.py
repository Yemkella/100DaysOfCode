#Number Guessing Game Objectives:

# Include an ASCII art logo. ✅
# Allow the player to submit a guess for a number between 1 and 100. ✅
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. ✅
# If they got the answer correct, show the actual answer to the player. ✅
# Track the number of turns remaining. ✅
# If they run out of turns, provide feedback to the player. ✅
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode). ✅

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
number = random.randrange(1, 100)
print("I'm thinking of a number between 1 and 100.")

difficulty = 'null'
while difficulty != 'easy' and difficulty != 'hard':
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  attempts = 10
else:
  attempts = 5


while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess_not_number = True
  while guess_not_number == True:
    try:
      guess = int(input("Make a guess: "))
      guess_not_number = False
    except ValueError:
      print("This is not a number!")
      guess_not_number = True
  if guess != number:
    attempts -= 1
    if guess > number:
      print("Too high.")
    else:
      print("Too low.")
  else:
    print(f"You got it! The answer was {number}.")
    exit()

if attempts == 0:
  print("You've run out of guesses. You lose! ")
  exit()
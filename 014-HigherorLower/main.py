import random
import os
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
from game_data import data
from art import logo
from art import vs
end_of_game = False
score = 0
print(logo)

# Establish a while loob so the game keeps going so long as end of game is false.
while end_of_game == False:
  
  # Establish 1st set of information
  array_1 = random.randint(0, 49)
  entry_1 = data[array_1]
  name_1 = entry_1['name']
  followers_1 = entry_1['follower_count']
  description_1 = entry_1['description']
  country_1 = entry_1['country']
  print(f"Compare A: {name_1}, a {description_1}, from {country_1}.")
  
  print(vs)
  
  # Establish 2nd set of information
  array_2 = random.randint(0, 49)
  entry_2 = data[array_2]
  name_2 = entry_2['name']
  followers_2 = entry_2['follower_count']
  description_2 = entry_2['description']
  country_2 = entry_2['country']
  print(f"Compare B: {name_2}, a {description_2}, from {country_2}.")

  # Variable 'winner' will be used to determine if the user input matches or not
  if followers_1 > followers_2:
    winner = 'a'
  else:
    winner = 'b'
  
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  # Checks to see if the user's input matches the 'winner' variable value
  if answer == winner:
    score += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {score}.")
    # Test code to ensure code was functioning properly
    # print(data[array_1])
    # print(data[array_2])
  else:
    end_of_game = True

clear()
print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
# Test code to ensure code was functioning properly
# print(data[array_1])
# print(data[array_2])
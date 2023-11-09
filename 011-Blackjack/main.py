############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

## cards in deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## defined functions
def player_draw():
  player_card = random.choice(cards)
  player_hand.append(player_card)
def computer_draw():
  computer_card = random.choice(cards)
  computer_hand.append(computer_card)
def you_lose():
  print(f"Your final hand: {player_hand} final score: {player_score}")
  print(f"Computer's final hand: {computer_hand} final score: {computer_score}")
  print("You lose!")
  exit()
def you_win():
  print(f"Your final hand: {player_hand} final score: {player_score}")
  print(f"Computer's final hand: {computer_hand} final score: {computer_score}")
  print("You win!")
  exit()
def tie():
  print(f"Your final hand: {player_hand} final score: {player_score}")
  print(f"Computer's final hand: {computer_hand} final score: {computer_score}")
  print("It's a draw!")
  exit()

## Start of program
play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_blackjack == 'n':
  exit()

## Set player hand and score
player_hand = []
player_score = 0

## Set computer hand and score
computer_hand = []
computer_score = 0

## Start game
print(logo)
player_draw()
player_draw()
while computer_score < 17:
  computer_score = 0
  computer_draw()
  for card in computer_hand:
    computer_score += card
first = computer_hand[0]
for card in player_hand:
  player_score += card
print(f"Your cards: {player_hand}, current score: {player_score}")
print(f"Computer's first card: {first}")
hit = input("Type 'y' to get another card, type 'n' to pass: ")

while hit == 'y':
  player_draw()
  player_score = 0
  for card in player_hand:
    player_score += card
  while player_score > 21 and 11 in player_hand:
    target_index = player_hand.index(11)
    player_hand[target_index] = 1
    player_score = 0
    for card in player_hand:
      player_score += card
  if player_score < 22:
    print(f"Your cards: {player_hand}, current score: {player_score}")
    print(f"Computer's first card: {first}")
    hit = input("Type 'y' to get another card, type 'n' to pass: ")  
  else:
    hit = 'n'
    you_lose()

if player_score == 21:
  player_score = 0
if computer_score == 21:
  computer_score = 0

if player_score > 21 and computer_score > 21:
  you_lose()
elif computer_score == player_score:
  tie()
elif computer_score == 0:
  print("Computer has Blackjack")
  you_lose()
elif player_score == 0:
  print("You have a Blackjack")
  you_win()
elif player_score > 21:
  you_lose()
elif computer_score > 21:
  you_win()
elif player_score > computer_score:
  you_win()
else:
  you_lose()


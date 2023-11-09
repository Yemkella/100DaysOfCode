import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def winner(users):
  highest_bid = 0
  highest_bidder = ""
  for name in users:
    if users[name] > highest_bid:
      highest_bidder = name
      highest_bid = users[name]
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
    

print(logo)
print("Welcome to the secret auction program.")

users = {}
other_bidders = True

while other_bidders == True:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  users[name] = bid
  more_bidders_prompt = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if more_bidders_prompt == 'no':
    other_bidders = False
  clear()


winner(users)
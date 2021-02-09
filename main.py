from replit import clear
from art import logo
print(logo)
continue_bid = True
players = {}

def highest_bidder(bid_record):
  highest_bid = 0
  for bidder in bid_record:
    bid_amount = int(bid_record[bidder])
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with the highest bid of ${highest_bid}")

while continue_bid == True:
  player_name = input("What is your name?").capitalize()
  player_bid = input("What is your bid? $")

  # add to dictionary
  players[player_name] = player_bid


  result = input('Do you wish to continue? Yes or No').lower()

  if result == 'yes':
    continue_bid = True
  else:
    continue_bid = False

    print(highest_bidder(players))

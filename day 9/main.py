import os
from ascii_art import logo

def max_bid(secret_auction):
  max_bid = 0
  for bidder in secret_auction:
    bid = secret_auction[bidder]
    if bid > max_bid:
      max_bid = bid

  return [
          max_bid,
          bidder,
         ]


secret_auction= {}

print(logo)
name =input('What is your name ? :')
bid = int(input("What's your bid ? : "))

secret_auction[name] = bid


confirm=True
while confirm==True:
  def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

  other_bidders = input('want to continue ? : ')
  if other_bidders == 'yes':
    name =input('What is your name ? :')
    bid = int(input("What's your bid ? : $"))
    secret_auction[name] = bid
  elif other_bidders =='no':
    confirm=False
  else:
    print("Are there any other bidders ? :(type 'yes' or 'no )  .\n"  )
    confirm = False



max = max_bid(secret_auction)
print(f'the winner is {max[1]} with a bid of ${max[0]}. ')

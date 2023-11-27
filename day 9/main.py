
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

name = input('your name : ?')
bid = int(input('your bid'))
secret_auction[name] = bid
confirm=True
while confirm==True:
  other_bidders = input('want to continue ? : ')
  if other_bidders == 'yes':
    name =input('your name : ?')
    bid = int(input('your bid'))
    secret_auction[name] = bid
  elif other_bidders =='no':
    confirm=False
  else:
    print('please type yes or no')
    confirm = False

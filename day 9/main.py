


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
import random
from ascii_art import welcomig_logo
#print the welcome message
print(welcomig_logo)
print('Welcome to the Number Guessing Game .')
print("I'm thinking of a number between 1 and 100 .")

# picking random number between 1 and 100
number = random.randint(1,100)
attempts =15
#choose a difficulty

difficulty_level=input("Choose a difficulty ? type 'e' for easy , 'h' for hard and 'm' for medium : (the default is easy)\n")
# 'easy'
if difficulty_level == 'm':
  attempts = 10
# 'hard'
elif difficulty_level == 'h': 
  attempts = 5



print(number)
end_of_game =False
#inside a while loop 5 for easy , and 10 for hard
while attempts>0 and end_of_game==False:

  #telling the user how many attempts are left
  if attempts ==1 :

    print(f"You have 1 attempt left 😬 😬")
  else:
    print(f"You have {attempts} attempts left")

  #asking the user to guess the number
  guess = int(input("Make a guess : "))

  #checking if the user guessed correctly
  if guess == number:
    print("You won !! 🥳 🥳")
    end_of_game = True
  #telling the user if they guessed correctly or not if they did print you win and exit the loop
  elif guess <number:
    attempts-=1
    print("Too Low")
  elif guess > number:
    attempts-=1
    print("Too High")
    # if (attempts == 0) print you lost
  if attempts == 0:
      print("You lost !! 🥲 🥲")


from data import data
import random
from art import logo,vs
import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

SCORE = 0
END_OF_GAME = False
print(logo)

def compare_followers(first_person,second_person):
  if first_person['followers']>second_person['followers']:
    return first_person
  else:
     return second_person
# def game():
#   global SCORE
#   for dictionary in data:
#     for key in dictionary:
#       first_person = dictionary[key[SCORE]]
#       second_person = dictionary[key[SCORE+1]]
#       print("compare these two :")
#       print(f"A: {first_person}")
#       print(vs)
#       print(f"B: {second_person}")
#       guess = input("Who has more followers ? Type 'A' or 'B'(default B) : ")
#       has_more_followers = compare_followers(first_person,second_person)
#       if guess == 'A'or guess=='a':
#         if has_more_followers == first_person:
#           print("Correct! 😁 😁")
#           SCORE+=1
#           game()
#         else:
#           print(f"You lost 😥 😥 , Final Score : {SCORE} ")
#           break


# game()

def game():
  global SCORE,END_OF_GAME

  while SCORE in range(len(data) - 1) and END_OF_GAME == False:
    index = random.randint(0,len(data)-1)
    first_person = data[index]
    index = random.randint(0,len(data)-1)
    second_person = data[index + 1]
    print("compare these two :")

    print(f"A: {first_person['name']},a {first_person['description']},from {first_person['followers']},")
    
    print(vs)
    
    print(f"B: {second_person['name']},a {second_person['description']},from {second_person['followers']}")

    guess = input("Who has more followers ? Type 'A' or 'B' : ")
    
    has_more_followers = compare_followers(first_person,second_person)
    
    if (guess.lower() == 'a' and has_more_followers == first_person)or (guess.lower()== 'b' and has_more_followers==second_person):
      clear_terminal()
      print("Correct! 😁 😁")
      SCORE+=1
    else:
      clear_terminal()
      print(f"You lost 😥 😥 , Final Score : {SCORE} ")
      END_OF_GAME= True
      return 0

game()

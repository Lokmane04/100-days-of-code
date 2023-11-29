from data import data
from art import logo,vs
SCORE = 0

print(logo)

def compare_followers(first_person,second_person):
  return first_person
def game():
  global SCORE
  for dictionary in data:
    for key in dictionary:
      first_person = dictionary[key[SCORE]]
      second_person = dictionary[key[SCORE+1]]
      print("compare these two :")
      print(f"A: {first_person}")
      print(vs)
      print(f"B: {second_person}")
      guess = input("Who has more followers ? Type 'A' or 'B'(default B) : ")
      has_more_followers = compare_followers(first_person,second_person)
      if guess == 'A'or guess=='a':
        if has_more_followers == first_person:
          print("Correct! 😁 😁")
          SCORE+=1
          game()
        else:
          print(f"You lost 😥 😥 , Final Score : {SCORE} ")
          break


game()


#rps stands for rock paper scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_tools = [rock,paper,scissors]
user_choice = int(input('type 1 for paper ,2 for scissors and 3 for  rock : '))

if(user_choice>3 or user_choice<=0):
  print('You typed an invalid number , please try again (number should be between 1 and 3) 😊')


computer_choice = random.randint(0,2) 

print('you choose :\n',game_tools[user_choice-1])

print('computer choose : \n',game_tools[computer_choice -1])

if((computer_choice==3 and user_choice==1) or (computer_choice>user_choice)):
  print('you win 🏆 🏆')
elif(user_choice == computer_choice):
  print("it's a draw 😮 😮")
else:
  print('you lose 🥲 🥲')

# import random
# def Print_output(output):
#  print(' '.join(output))



# def word_found(word):
#     letter_found = True
#     for letter in word:
#         if letter == '_':
#             letter_found = False
#     return letter_found



# def replace_letter(user_input,chosen_word):
#   letter_found = False
#   for i in range(len(chosen_word)):
#       if user_input == chosen_word[i]:
#         output[i] = user_input
#         letter_found = True
#   return letter_found


# def blank_word(output,word):
#   for _ in word:
#    output.append('_')




# words_list = ["Example", "Library", "Science", "History", "Natural", "Culture", "Society", "Economy", "Industry", "Politics", "Language", "Education", "Research", "Software", "Hardware", "Internet", "Database", "Network", "Security", "Strategy"]
# output = []
# count = 0
# chosen_word = random.choice(words_list).lower()
# blank_word(output,chosen_word)

# print(chosen_word)





# #user input
# for i in range(len(chosen_word)):
#   if count ==5:
#     break
#   elif not word_found(output):
#       user_input = input("Guess a letter: ").lower()
    
#       if not replace_letter(user_input,chosen_word):
#           count += 1
#           print(f'You made {count} mitake(s)')
#       else :Print_output(output)
      
#   else: 
#       print('You found the word !!! 🥳 🥳') 
#       break

# if count ==5 : print('You lost !! 🥲 🥲')


# second solution
import random
from hangman_words import word_list,stages,hangman_logo
import os
print(hangman_logo)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

end_of_game = False

chosen_word = random.choice(word_list).lower()
chosen_word_length = len(chosen_word)

lives = 6
display = []
for _ in range(chosen_word_length):
   display+= '_'




while not end_of_game:
    guess = input('Guess a letter :').lower()
    clear_terminal()
    if guess in display:
      print(f"you've already guessed {guess}, try again . ")
    for index in range(chosen_word_length):
      letter = chosen_word[index]
      
      if guess == letter :
          display[index] = letter
          print(' '.join(display))
      
      
    if guess not in chosen_word:
      lives-=1
      print(stages[lives])
      print(f"you guessed the letter '{guess}' and it's not in the word, you lose a life !!")
      if lives == 0:
        print('You Lost !! 🥲 🥲')
        end_of_game = True


    if '_' not in display : 
      print('You won !! 🥳 🥳 ')   
    
      

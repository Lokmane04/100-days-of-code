import random
def Print_output(output):
 print(' '.join(output))



def word_found(word):
    letter_found = True
    for letter in word:
        if letter == '_':
            letter_found = False
    return letter_found



def replace_letter(user_input,chosen_word):
  letter_found = False
  for i in range(len(chosen_word)):
      if user_input == chosen_word[i]:
        output[i] = user_input
        letter_found = True
  return letter_found


def blank_word(output,word):
  for _ in word:
   output.append('_')




words_list = ["Example", "Library", "Science", "History", "Natural", "Culture", "Society", "Economy", "Industry", "Politics", "Language", "Education", "Research", "Software", "Hardware", "Internet", "Database", "Network", "Security", "Strategy"]
output = []
count = 0
chosen_word = random.choice(words_list).lower()
blank_word(output,chosen_word)

print(chosen_word)





#user input
for i in range(len(chosen_word)):
  if count ==5:
    break
  elif not word_found(output):
      user_input = input("Guess a letter: ").lower()
    
      if not replace_letter(user_input,chosen_word):
          count += 1
          print(f'You made {count} mitake(s)')
      else :Print_output(output)
      
  else: 
      print('You found the word !!! 🥳 🥳') 
      break

if count ==5 : print('You lost !! 🥲 🥲')

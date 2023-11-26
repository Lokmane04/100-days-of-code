alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(word,shift):
  new_word = ''.join([alphabet[(alphabet.index(letter) + shift) % len(alphabet)] for letter in word])
  return new_word



def hashe(direction,text,shift):
    if direction == 'encode' or direction=='1':
      return encrypt(text,shift)
    elif direction == 'decode' or direction == '2':
      return encrypt(text,-shift)
    else:
       return "please type in 'encode'or 'decode'"
  
  

direction = input("Type 'encode' or 1 to encrypt, type 'decode' or 2 to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number (must be positif in both cases):\n"))

print(hashe(direction,text,shift))
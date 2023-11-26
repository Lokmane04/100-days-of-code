alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(word,shift):
  new_word =''
  for letter in word: 
        new_word+= alphabet[int(alphabet.index(letter)%len(alphabet))+shift]
  return new_word


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# print(encrypt_decrypt('hello',5))

def hashe(direction,text,shift):
    if direction == 'encode' :
      return encrypt(text,shift)
    elif direction == 'decode' :
      return encrypt(text,-shift)
    else:
       return "please type in 'encode'or 'decode'"
  

direction = input("type encode or decode :\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number :\n"))

print(hashe(direction,text,shift))
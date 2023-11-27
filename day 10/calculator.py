from ascii_art import logo
import os
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculator(number):
  operation = input("\n- \n+ \n/ \n*\nPick an operation : ")
  number2 = float(input("What's the second number ? : "))
  result = int(number)
  if operation == '+':
    result = result + float(number2)
  elif operation == '-':
    result = result - float(number2)
  elif operation == '*':
    result = result * float(number2)
  elif operation == '/':
    result = result / float(number2)
  else :
    print('Please type a valid operation .')
  print(f"The result is {result} ")
  return result

print(logo)
number1 = (float)
result =calculator(number1)

confirm = True
while confirm == True:
  continue_operation = input(f"Type 'y' to continue calculating on {result} , type 'n' to start new calculation, 'q' to quit: ")
  if continue_operation == 'y':
    clear_terminal()
    result = calculator(result)    
  elif continue_operation == 'n':
    clear_terminal()
    number = float(input("What's the first number ? : "))
    result =calculator(number)
  elif continue_operation =='q':
    print("Thank you for using our calculator .")
    confirm =False
  else:
    print("Please type 'n' or 'y' or 'q' .")
    print("Thank you for using our calculator .")
    confirm = False
def calculator(number):
  operation = input("\n- \n+ \n/ \n*\nPick an operation : ")
  number2 = input("What's the second number ? : ")
  result = int(number)
  if operation == '+':
    result = result + int(number2)
  elif operation == '-':
    result = result - int(number2)
  elif operation == '*':
    result = result * int(number2)
  elif operation == '/':
    result = result / int(number2)
  else :
    print('Please type a valid operation .')
  print(f"The result is {result} ")
  return result


number1 = input("What's the first number ? : ")
result =calculator(number1)

confirm = True
while confirm == True:
  continue_operation = input(f"Type 'y' to continue calculating on {result} , type 'n' to start new calculation, 'q' to quit: ")
  if continue_operation == 'y':
    result = calculator(result)    
  elif continue_operation == 'n':
    number = input("What's the first number ? : ")
    result =calculator(number)
  elif continue_operation =='q':
    print("Thank you for using our calculator .")
    confirm =False
  else:
    print("Please type 'n' or 'y' or 'q' .")
    print("Thank you for using our calculator .")
    confirm = False
def calculator(number):
  operation = input("Pick an operation : \n- \n+ \n/ \n*\n")
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
  continue_operation = input(f"Type 'y' to continue calculating on {result} , type 'n' to start new calculation ")
  if continue_operation == 'y':
    result = calculator(result)    
  elif continue_operation == 'n':
    number = input("What's the first number ? : ")
    calculator(number)
  
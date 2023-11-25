
def prime_checker(number):
    if number ==0:
        return False
    if number == 2 or number==1:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, ( number / 2 ) + 1):
        if number % i == 0:
            return False
    return True

user_input = int(input('Check this number : '))
is_prime = prime_checker(user_input)
print(is_prime)
if is_prime:
    print(f'{user_input} is a prime number')
else:
    print(f'{user_input} is not a prime number')

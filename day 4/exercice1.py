import random
names = input('Type in the names , separate them with comma the n a space (eg: eimane, habib, lokmane) : ').split(', ')
# first solution
print(names[random.randint(0,len(names)-1)],'is going to pay for dinner 🥲 🥲')
# second solution , more optimized
# print(random.choice(names))
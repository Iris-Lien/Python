import random
password = random.randint(1,100)
hit = False
answer = int(input('Please guess a number between 1 and 100:'))
while not hit:
    if answer==password:
        print('Correct answer!')
        hit = True
    elif answer<password:
        answer = int(input('Too small, please guess again:'))
    elif answer>password:
        answer = int(input('Too large, please guess again:'))
print('The game is over.')

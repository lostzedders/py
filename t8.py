import random
num = random.randint(1, 100)
guess_num = int(input('Enter a number you guess'))
time = 0
while guess_num != num:
    if guess_num > num:
        print('bigger')
    elif guess_num < num:
        print('smaller')
    guess_num = int(input('reEnter a number you guess'))
    time += 1
print('the result is %s,time is %s' % (num, time))
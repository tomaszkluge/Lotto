import random

play = 'yes'

give = []
back = []

while play == 'yes':
    for i in range(6):
        give.append(int(input('Enter a number: '+str(i+1)+': ')))
        back.append(random.randint(1, 50))
    correct = 0
    for z in give:
        for y in back:
            if z == y:
                correct += 1
    print('You got '+str(correct)+' correct')
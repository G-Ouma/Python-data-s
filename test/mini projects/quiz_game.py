print('Welcome to the Quiz Game!')

playing = input('Do you want to play (y/n)? ')
if playing.lower() != 'y':
    quit()

print("Ok! Let's start playing!")
score = 0

ans = input('What does CPU stand for? ')
if ans.lower() == 'central processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

ans = input('What does GPU stand for? ')
if ans.lower() == 'graphics processing unit':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

ans = input('What does RAM stand for? ')
if ans.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

ans = input('What does PSU stand for? ')
if ans.lower() == 'power supply':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('You have scored ' + str(score) + ' questions correctly!')
print("You have got " + str(int(score/4 * 100)) + '%')


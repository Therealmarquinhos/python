#lab 3: quiz

correct_answers = 0

q1 = raw_input("is your name Jeff? y/n: ")
if q1 == 'y':
    print('excellent Jeff, you get a point')
    correct_answers = correct_answers + 1
else:
    print'only Jeff\'s get a point'

q2 = int(raw_input('what is 2 + 2? '))
if q2 == 4:
    print('correct')
    correct_answers = correct_answers + 1

print('you have' , correct_answers, 'correct answers')
         

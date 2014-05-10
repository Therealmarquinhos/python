#camel game
import random

print 'Welcome to Camel!'
print 'You have stolen a camel to make your way across the great Mobi desert.'
print 'The natives want their camel back and are chasing you down! '
print 'Survive your desert trek and our run the natives.'

done = False

miles_travelled = 0
thirst = 0
camel_tired = 0
natives = -20
natives_t = 0
canteen = 3

def natives_behind(n_t, m_t): #function to calc how far the natives are behind.
    dist_behind = -20 + (n_t-m_t)
    return dist_behind

while not done:
    print'A. Drink from your canteen.'
    print'B. Ahead moderate speed.'
    print'C. Ahead full speed.'
    print'D. Stop and rest.'
    print'E. Status check.'
    print'Q. Quit.'
    
    answer = raw_input("What is your selection? ")

    if answer.upper() == "Q":
        done = True;
    elif answer.upper() == "E":
        print'Miles traveled: ', miles_travelled
        print'Drinks in canteen: ', canteen
        print'The natives are ',abs(natives_behind(natives_t, miles_travelled)), ' miles behind you'
        
    elif answer.upper() == "D":
        camel_tired = 0
        natives_t = natives_t + random.randrange(8, 13)
        print'The camels are rested and happy'
    elif answer.upper() == "C":
        thirst = thirst + 1
        camel_tired = camel_tired + random.randrange(1,3)
        miles_travelled = miles_travelled + random.randrange(10,20)
        natives_t = natives_t + random.randrange(8, 13)
        print'You have travelled ', miles_travelled, ' miles'
    elif answer.upper() == "B":
        thirst = thirst + 1
        camel_tired = camel_tired + random.randrange(1)
        miles_travelled = miles_travelled + random.randrange(5,12)
        natives_t = natives_t + random.randrange(8, 13)
        print'You have travelled ', miles_travelled, ' miles'
    elif answer.upper() == "A":
        if canteen > 0:
            canteen = canteen - 1
            thirst = thirst -1
            natives_t = natives_t + random.randrange(8, 13)
            print'Stopping for a dring. There are ', canteen, ' drinks left'
        else:
            print'No drinks left'
    
    if 4 < thirst <= 6:
        print'You are thirsty'
    elif thirst > 6:
        print'You died of thirst'
        done = True

    if 5 < camel_tired <=8:
        print'Your camel is getting tired'
    elif camel_tired > 8:
        print'Your camel is dead'
 
    if natives_behind(natives_t, miles_travelled) >= 0:
        print "You are dead"
        done = True
    
    if -15 < natives_behind(natives_t, miles_travelled) < 0 :
        print "The natives are getting close"
        
    if miles_travelled >= 200:
        print "You have won"
        done = True
        
    if random.randrange(0,6) == 4:
        print"You have found an oasis"
        canteen = 3
        thirst = 0
        camel_tired = 0
        
    


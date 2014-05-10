#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Award #time-and-a-half for the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to #test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the #string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

#ex3.1
#hrs = raw_input("Enter Hours:")
#h = float(hrs)
#rate = raw_input("Enter rate per Hour: ")
#r = float(rate)

#if h > 40:
#    print (40 * r) + ((h-40) * (r * 1.5))
#else:
#    print r * h
    
#raw_input("finish")

#ex 3.3
#3.3 Write a program to prompt the user for a score using raw_input. Print out a letter grade based on the following #table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.



score = raw_input("enter the score needed: ")
s = float(score)

if s >= 0.9:
    print "A"
elif s >= 0.8:
    print "B"
elif s >= 0.7:
    print "C"
elif s >= 0.6:
    print "D"
elif s < 0.6:
    print "F"
else: 
    print "Enter a valid number"

raw_input("finshed")







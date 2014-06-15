#week 9 

#9.4 Write a program to read through the mbox-short.txt and figure out who has the most
#commits. The program looks for 'From ' lines and takes the second word of those lines
#as the person who sent the mail. The program creates a Python dictionary that maps the
#senders mail address to a count of the number of times they appear in the file. After
#the dictionary is produced, the program reads through the dictionary using a maximum
#loop to find the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)


words = list()
person = list()


#creates a list of email addresses
def fromList():
    for line in handle:
        words = line.split()
    
        if len(words) == 0 :
            continue 
        if words[0] == 'From' :
            person.append(words[1])
    return person
    
#creates a dictionary and counts the number of times someones name appears        
def countFroms(lstToUse):
    d = dict()
    pers = lstToUse
    for p in pers:
        d[p] = d.get(p,0) + 1
    return d
   
def prolificCommitter():
    dict = countFroms(fromList())
    bigName = None
    bigCount = None
    
    for ff,cc in dict.items():
        if bigCount is None or cc > bigCount:
            bigName = ff
            bigCount = cc
    print bigName, bigCount
    return

prolificCommitter()

        

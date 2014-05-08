#!/usr/bin/env python

'''
Reads every line from a  hardcoded file
or skips the first line
And, counts every line
'''

'''
count = 0

with open ('1a1e_C.txt') as f:
    #next(f) #skips first row
    f.readline(0)# use f.readline(0) if need the header or first row
    for line in f:
        count += 1
        print (line)

print ("\nCount: " + str(count))
'''

#####

'''
As above, but the file is user input
'''

'''
InFile = input("Please enter the file name: ")

count = 0

with open (InFile) as f:
    #next(f) #skips first row
    f.readline(0)# use f.readline(0) if need the header or first row
    for line in f:
        count += 1
        print (line)

print ("\nCount: " + str(count))
'''
#####

'''
As above, but has two subroutines or functions
'''

def ReadLines(InFile):
    with open (InFile) as f:
        allLines = []
        #next(f) #skips first row
        f.readline(0)# use f.readline(0) if need the header or first row
        for line in f:
            #allLines += [line] # captures into array
            print(line.strip("\n")) #use just to read a file
    #return allLines # returns array

#def CountLinesAlt(InFile): #works for simple files, but not all
#    count = len(InFile)
#    return(count) #use to return a value

def CountLines(InFile):
    count = 0
    with open (InFile) as f:
        f.readline(0)
        for line in f:
            count += 1
            #print(count)
    return(count)

InFile = input("Please enter the file name: ")
print("") # one line of white space
ReadLines(InFile) #Function to read each line of the file
print("\nCount: ", CountLines(InFile)) # Function to count no. lines in file

    


# -*- coding: utf-8 -*-
#Arnav Lohe
#Finite State Machine
#Run in Python 2

def accept(inputString): #accepts the input string, checks whether the accept condition 1 -> 1 -> 0 -> 1 is in the string
    if '1101' in inputString: #S1, S2, S3, S4
        return True
    else:
        return False

def isValid(inputString): #accepts the input string, checks whether all the characters are valid binary input
    flag = True
    s = len(inputString)
    i = 0
    for i in range(s-3):
            if inputString[i] not in ['0', '1']: #S5
                flag = False
    return flag

def FSM(inputString): #function to simulate the finite state machine
    if accept(inputString) and isValid(inputString):
        print("String is accepted") #S4
    else:
        print("String is not accepted") #S5
            
def proceed(): #recursive function to run the finite state machine as many times as the user wants
    response = raw_input("Would you like to enter a binary string (y/n): ")
    if response == 'y':
        inputString = raw_input("Enter binary string: ")
        FSM(inputString)
        proceed()

proceed()

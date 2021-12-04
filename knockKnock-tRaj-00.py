'''
Program: Knock-Knock
Filename: knockKnock-tRaj-00.py
Author: Tushar Raj
Description: Simulates the knock knock joke game
Revisions: No revisions made
'''
import random #imports the random class to use choice for different
import time #import time to use sleep function so that before quit executes user get to read the output statement
count=0 #To keep track of how many jokes have been made

#Dictoniary containing Knock-Knock jokes
mydict = {"tank":"You're welcome.",
          "Nobel":"Nobel...that's why I knocked.",
          "Etch":"Please sneeze into your elbow!",
          "Cash":"No thanks, I prefer peanuts.",
          "Ya":"Yahoo! I’m happy to see you too!",
          "Boo":"Don't cry, it’s only a joke.",
          "Dwayne":"Dwayne the tub before I dwown.",
          "Adore":"Adore is between us, so open it!",
          "Noah":"Adore is between us, so open it!",
          "Kirtch":"God bless you!",
          "Justin":"Justin time for dinner.",
          "Impatient cow":"Mooooo!",
          "Two knee":"Two-knee fish!",
          "Abby":"Abby birthday to you!"}

#There are no class defined

def inputdata(number): #checks the user input is correct
    '''
    This function accepts the input from the user and checks if the value contains any special character,alphabets.It even checks that the value is not negative
    Input: user input from the console which is string type
    output: returns converted strings into int data type
    '''
    special = "!@#$%^&*().-|/,';:{]}[{\?+?_=,<>/"
    alphabet = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
    while True:
        if(any( i in alphabet for i in number)): #checks if the value entered in number variable is having any character or not
            print("****Can't understand what are you trying to say. The number of game should be a number not a characters****\n") #prints the error message
            progress = input("Please enter if you want to continue with knock-knock game(y/n): ") #ask users if he wants to continue with program
            if( progress == 'y' or progress == 'Y' ):#checks the response of the user if its yes, asks to enter the diameter again
                number = input("\nHello Friend ! how many knock-knock jokes you want to play today: ")
            if( progress == 'n' or progress == 'N' ):#exits the program if response in no
                exit()
            continue
        elif (any( i in special for i in number)): #picks up each character from the number variable and then checks in special variable if it is present, if present run this elif
            print("****Can't understand what are you trying to say. The number of game should be a number not a special characters or decimal number****\n")
            progress = input("\nPlease enter if you want to continue with knock-knock game(y/n):")
            if( progress == 'y' or progress == 'Y' ):
                number = input("\nHello Friend ! how many knock-knock jokes you want to play today: ")
            if( progress == 'n' or progress == 'N' ):
                exit()
            continue
        else:
            if(int(number) > len(mydict) or int(number)<=0): #checks that user dosent ask to play more number of games than program knows if yes as he want to play max no of jokes program knows
                x=(input(f"Friend! I only know {len(mydict)} Knock-knock. You want to play(y/n):")).lower()
                if( x == 'n'):
                    exit()
                if( x == 'y'):
                    number = input("Hello Friend ! how many knock-knock jokes you want to play today: ")
                    continue
            else:
                return number


### main program starts here
print("****Knock-Knock program****\n\n")#displays the starting of knock-knock program
joke_number = input("Hello Friend ! how many knock-knock jokes you want to play today: ") #ask user to input how many times he want to play game
numberOfGameplay = inputdata(joke_number)#call the function and store no of times game should be played
#numberOfGameplay=gameplay()
while True:
    print("\nKnock-knock!") #Print knock-knock to initiate the joke
    #considering different varient of user input in response of knock-knock
    whoVariant = ["whos there","who is there","who there","who dere","whos der","who is dere","who der"]

    #Initiating the loop to go through the joke
    while True:
        inputWhat = input() # accept the input from user in response of knock-knock
        inputWhat = "".join([i for i in inputWhat if i not in "!@#$%^&*()_'+{}|[]\:;<>,.?/"]).lower().strip() #remove special character from user input and change all character to lower for ease of comparing
        if inputWhat in whoVariant: # if user input matches with all possible varient proceed with next step of the joke
            jokePart1,jokePart2=random.choice(list(mydict.items())) #Randomly pick up a joke from the Dictoniary of knock-knock joke
            print(jokePart1) #print the second response of computer
            inputDict = input() #accept the user input as response 
            inputDict_noSpecial = "".join([i for i in inputDict if i not in "!@#$%^&*()_'+{}|[]\:;<>,.?/"]).lower().strip() #remove the special character from response and covert to lower for ease of comparing
            valueExpected = (jokePart1+" who").lower() #store expected value in a variable
            while True:
                if(inputDict_noSpecial == valueExpected): #Compare if the user input is same as expected input
                    print(jokePart2) #print the final part of the joke
                    mydict.pop(jokePart1)#deletes the jokes which has been made
                    count+=1
                    break
                else:
                    print("Sorry.  The correct response is \"{} who?\"".format(jokePart1)) #print the error when user response dosent match
                    print("Try again\n")
                    print(jokePart1)
                    inputDict = input() #accept the user input as response 
                    inputDict_noSpecial = "".join([i for i in inputDict if i not in "!@#$%^&*()_'+{}|[]\:;<>,.?/"]).lower().strip() #remove the special character from response and covert to lower for ease of comparing
                    continue #continue with the loop
        else:
            print("Sorry.  The correct response is \"Who's there?\"") #print the error when user response dosent match for who's there condition
            print("Try again.\n")
            print("Knock-knock!") #Print knock-knock to initiate the joke again
            continue #continue with the loop
        break
    if(len(mydict)==0 or count == int(numberOfGameplay)):#checks if the joke dictonary is empty or the no of jokes user what has reached or not if yes then terminate the program
        break
    
print("\n\n****Knock-Knock program has ended****")#displays the end of knock knock program

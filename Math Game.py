import math
import random

def randomCalc(ops, digit):#This function creates the random question that is asked, it's two inputs define the level it needs
    num1 = random.randint(0,math.pow(10,digit))
    num2 = random.randint(0,math.pow(10,digit))
    op = random.choice(ops)
    answer = eval(str(num1) + op + str(num2))
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer

def GameStart():
    totaloperations = ['+','-','*','/','%']
    print ("Welcome to the random math question game!\n\n\n")
    Total_Errors = 0
    for level in range(5):#Iterate through each level
        stars_that_level = 0#Amount of values they solved correctly
        print ("Level %d:\nPossible length of Numbers:%d\nPossible number of Operators:%d"%((level+1),max(1,(level+1)/2),(level+1)))
        for question in range(5):#Iterate through each question
            correctvalue = randomCalc(totaloperations[:level+1],max(1,(level+1)/2))
            WrongInput = True
            while WrongInput:#Repeat until we get suitable input

                #Print out the correct amount of stars that round
                allstars =''
                for numofstars in range(stars_that_level):
                    allstars+='*'
                if allstars != '':
                    print (allstars)

                attemptedvalue = input(">>>")
                for i in attemptedvalue:
                    if ((i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9' and i!='-')):#BONUS: Check if the value is correct or not
                        WrongInput = True
                        print ("ERROR! Un-acceptable entry detected, try again please!\n")
                        break
                    else:
                        WrongInput = False

            if (int(attemptedvalue)==correctvalue):#First convert the value into an integer, and check if the answer is correct
                stars_that_level+=1
                print ("Correct! You gain an additional star! You now have %d out of five stars!"%(stars_that_level))
            else:
                Total_Errors += 1#Add onto the total errors
                print ("Wrong! You do not gain any stars for that question!\nYou name have %d out of five stars!"%(stars_that_level))
        if (stars_that_level>=3):#Checks if there are enough stars
            print ("You have enough stars this level, time to move on!")
        else:
            print ("You do not have enough stars to move on to the next level, this as far as you go!")
            return
    print ("Amazing! You beat the game! You answered a total of %d answers wrong this attempt"%(Total_Errors))

GameStart()
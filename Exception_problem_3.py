#  Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

def ask():
    while True:
        try:
            n = int(input('Input an integer: '))
        except:
            print('An error occurred! Please try again!')
            continue
        else:
            break
            
     print('Thank you, your number squared is: ',n**2)
    
ask()

'''
OUTPUT

Input an integer: d
An error occurred! Please try again!
Input an integer: 7
Thank you, your number squared is:  49
'''

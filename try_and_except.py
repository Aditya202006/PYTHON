def number():
    while True:
        try:
            result=int(input('Enter number :'))
        except:
            print("It's not a number")
        else:
            print('Thank you')
            break
number()

'''
OUTPUT

Enter number :Hello
It's not a number

Enter number :50k
It's not a number

Enter number :7
Thank you
'''

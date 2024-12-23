# Try,Except and finally 

try:
    f=open('testfile','r')
    f.write('write a test line')
except:
    print('There is a Exception')
finally:
    print('This peace of code always run.')

'''
OUTPUT:

There is a Exception
This peace of code always run.
'''

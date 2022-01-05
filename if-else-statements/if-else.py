# Samples of sintaxis
'''
value = 'antonymont' # Declare variable
flag = True

if flag:
    # The if keyword
    if value == 'antoinemon': # The required colon ":" character
        print('The value is ' + value) # Require identation
    elif value == 'antoinemon_':
        print('The value is ' + value)
    elif value == 'antonymont':
        print('The value is ' + value)
    else: 
        print('The value is not ' + value)

print('Finished!')

print(type('Hello world'))
print(type(7))
print(type(True))
print(type('True'))

print(bool(0))
print(bool(1))
'''

# Branch code execution based on user input

isContinue = input('Would you like to continue? ')
if bool(isContinue) and (isContinue == 'yes' or isContinue == 'y'):
    print('Continuing ...')
    print('Complete!')
elif bool(isContinue) and (isContinue == 'no' or isContinue == 'n'):
    print('Exiting')
else:
    print('Please try again and respond with yes or no.')
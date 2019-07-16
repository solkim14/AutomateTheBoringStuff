#what to do if it's raining

print('start - answer yes or no')

print('is raining?')
userInput1 = input()
if (userInput1=='yes'):
    print('have umbrella?')
    userInput2 = input()
    if (userInput2 != 'yes'):
        userInput3=''
        while (userInput3!='no'):
            print('wait a while')
            print('is it raining?')
            userInput3 = input()
print('go outside')

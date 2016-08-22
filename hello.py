# This program says hello and asks for my name.

print('Hello world!')       # Python CALLS print FUNCTION, passes string as ARGUMENT
print('What is your name?')
myName = input()        # accept user input using 'input()'
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))      # string LENGTH given by 'len()'
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in  a year.')

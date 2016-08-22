Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello world!')
Hello world!
>>> print("Hello world!")
Hello world!
>>> 
2+2
4
>>> # surround Strings in 'SINGLE QUOTES'
>>> 

>>> 6*5
30
>>> 30/5
6.0
>>> # division always returns a FLOATING POINT number
>>> 
>>> 
tax = 12.5/100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_,2)
113.06
>>> # when in interactive mode, the last printed value is assigned to the UNDERSCORE character
>>> 
>>> a = ""
>>> a
''
>>> a = ''
>>> a
''
>>> a =
SyntaxError: invalid syntax
>>> letterList[] = {'a', 'b', 'd', 'q', 'g', 'x'}
SyntaxError: invalid syntax
>>> letterList {'a', 'b', 'd', 'q', 'g', 'x'}
SyntaxError: invalid syntax
>>> letterList = {'a', 'b', 'd', 'q', 'g', 'x'}
>>> letterList
{'x', 'b', 'g', 'a', 'd', 'q'}
>>> for(int i = 0; i < letterList.Length; i++)
SyntaxError: invalid syntax
>>> a = 'ba' + 'boo'
>>> a
'baboo'
>>> a += str(42069)
>>> a
'baboo42069'
>>> # CAST int 42069 as string using 'str()'
>>> 
>>> myface5 = 'myFace' * 5
>>> myface5
'myFacemyFacemyFacemyFacemyFace'
>>> 
>>> 
== RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/hello.py ==
Hello world!
What is your name?
Sam
It is good to meet you, Sam
The length of your name is: 
3
What is your age?
24
You will be 25 in  a year.
>>> 
>>> # CASTING examples
>>> 
>>> str(0)
'0'
>>> str(-3.14)
'-3.14'
>>> float(1)
1.0
>>> float(a)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float(a)
NameError: name 'a' is not defined
>>> float(0)
0.0
>>> int(3.14)
3
>>> int(3.99)
3
>>> spam = input()
101
>>> spam
'101'
>>> spam = int(spam)
>>> spam
101
>>> # int() ROUNDS a float argument down, while 'int() + 1' ROUNDS up
>>> 
>>> # input() ALWAYS RETURNS A STRING, even if user enters a number
>>> 
>>> # an integer CAN BE EQUAL to a floating point

>>> 42 == '42'
False
>>> 42 == 42.0
True
>>> 42 == 042.00000
True
>>> round(3.5)
4
>>> round(3.4999)
3
>>> pi
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> circ = 2*pi*r
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    circ = 2*pi*r
NameError: name 'pi' is not defined

>>> 5 == 5
True
>>> # BINARY BOOLEAN OPERATORS: 'and' 'or' 'not'
>>> 
>>> me and me
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    me and me
NameError: name 'me' is not defined
>>> me = ''
>>> you = ''
>>> me and you
''
>>> True and True
True
>>> me or you
''
>>> me = 5
>>> you = 4
>>> me and you
4
>>> me or you
5
>>> me not you
SyntaxError: invalid syntax
>>> you not me
SyntaxError: invalid syntax
>>> me == you
False
>>> me != you
True
>>> not True
False
>>> not False
True
>>> # language programmed in BLOCKS of code
>>> 
>>> # loops and conditions are blocked by INDENTS
>>> 
>>> name
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> name = 'Bob'
>>> if name == 'Alice':
	print('Hi, Alice.')

	
>>> name = 'Alice'
>>> if name == 'Alice':
	print('Hi, Alice.')

	
Hi, Alice.
>>> if name == 'Bob':
	print('Hi Bob')
else:
	print('Hello STRANGER???')

	
Hello STRANGER???
>>> if name == 'Bob'
SyntaxError: invalid syntax
>>> if name == 'Bob':
	print('Suh')
elif name == 'A':
	print('Dude')
else:
	print('Woah')

	
Woah
>>> name
'Alice'

>>> spam = 0
while spam < 5:
	
SyntaxError: multiple statements found while compiling a single statement
>>> spam = 0
>>> while spam < 5:
	print('Looping, round #' + spam)
	spam = spam + 1

	
Traceback (most recent call last):
  File "<pyshell#113>", line 2, in <module>
    print('Looping, round #' + spam)
TypeError: Can't convert 'int' object to str implicitly
>>>  while spam < 5:
	print('Looping, round #' + (str)spam)
	spam = spam + 1
	
SyntaxError: unexpected indent
>>> while spam < 5:
	print('Looping, round #' + (str)spam)spam = spam + 1
	
SyntaxError: invalid syntax
>>> while spam < 5:
	print('loop #' + (str)spam
	      
SyntaxError: invalid syntax
>>> while spam < 5:
	print('loop #' + (str)spam)
	
SyntaxError: invalid syntax
>>> print('words ' + (str)spam)
SyntaxError: invalid syntax
>>> spam
0
>>> spam = (str)spam
SyntaxError: invalid syntax
>>> spam = 1
>>> spam
1
>>> spam = (str)spam
SyntaxError: invalid syntax
>>> print('loop #' + str(spam))
loop #1
>>> spam = 0
>>> while spam < 5:
	print('loop #' + str(spam)
	      spam ++
	      
SyntaxError: invalid syntax
>>>  while spam < 5:
	print('loop #' + str(spam)
	      spam += 1
	      
SyntaxError: unexpected indent
>>> while spam < 5:
	print('loop #' + str(spam)
	spam += 1
	      
SyntaxError: invalid syntax
>>> while spam < 5:
	print('loop #' + str(spam)
	spam = spam + 1
	      
SyntaxError: invalid syntax
>>> while spam < 5:
	print('loop #' + str(spam))
	spam += 1

	
loop #0
loop #1
loop #2
loop #3
loop #4
>>> # WHILE LOOP condition checked at the start of each loop iteration
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/yourName.py 
Please enter your name.
Sam
Please enter your name.
Drew
Please enter your name.
your name
Thank you!
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/yourName2.py 
Type your name.
sam
Type your name.
me
Type your name.
you
Type your name.
!D!OMN
Type your name.
your name
You escaped the infinite loop
>>> # BREAK statement immediately exists the while loop
>>> # CONTINUE causes program to jump back to start of loop and evaluate conditions
>>> 
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/swordFish.py 
Who are you?
me
Who are you?
john
Who are you?
Sam
What is the password?
wang
Who are you?
Sam
What is the password?
mattress
Come on up. Impressive sir!
Who are you?

 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/swordFish.py 
Who are you?
me
Who are you?
Sam
What is the password?
mattress
Come on up. Impressive sir!
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/fiveTimes.py 
My name is
Jimmy Five Times (0)
Jimmy Five Times (1)
Jimmy Five Times (2)
Jimmy Five Times (3)
Jimmy Five Times (4)
>>> # range(5) includes 0-4, does excludes 5
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/fiveTimes.py 
Traceback (most recent call last):
  File "C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/fiveTimes.py", line 9, in <module>
    print('the sum from 0-100 is: ' + i)
TypeError: Can't convert 'int' object to str implicitly
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/fiveTimes.py 
the sum from 0-100 is: 101
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/fiveTimes.py 
the sum from 0-100 is: 5050
>>> range(5,-1,1)
range(5, -1)
>>> for i in range(5, -1, 1)
SyntaxError: invalid syntax
>>> for i in range(5, -1, 1):
	print(i)

	
>>> for i in range(5, -1, -1):
	print(i)

	
5
4
3
2
1
0
>>> import random
for i in range(5):
    print(random.randint(1, 10))
    
SyntaxError: multiple statements found while compiling a single statement
>>> import random
for i in range(5):
    print(random.randint(1, 10))
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/printRandom.py 
4
2
1
7
7
>>> 
 RESTART: C:/Users/Sam P/Documents/GitHub/AutomateTheBoringStuff/printRandom.py 
9
4
1
9
5
>>> # import multiple modules in one line as follows: 'import random, os, sys, math'
>>> # FROM statement eliminates need for module prefix: 'from random import *'
>>> 
>>> 
>>> # terminate a running program: 'sys.exit()'

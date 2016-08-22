name = ''
while True:
    print('Who are you?')
    name = input()
    if name != 'Sam':
        continue    # returns to beginning of loop
    else:
        print('What is the password?')
        password = input()
        if password == 'mattress':
            break
        else:
            continue
print('Come on up. Impressive sir!')

from random import randint
alphaLower = 'abcdefghijklmnopqrstyvwxyz'
alphaUpper = 'ABCDEFGHIJKLMNOPQRSTYVWXYZ'
symbols = '(^:?+){/!&$;#,@'

size = input("How long do you want your password?")
symbolCheck = input(f"Do you want to have symbols? ie: {symbols}")

#Time to generate the password

#Elements that will make the password
tempPass = ''

#Select some lowers

for i in range(randint(a, size-(int(size/3)))):
    print('i')

from random import randint, shuffle

symbols = '(^-:?+){/!&$;#,@0123456789'

size = int(input("How long do you want your password?"))
#symbolCheck = input(f"Do you want to have symbols? ie: {symbols}")

#Time to generate the password

#Elements that will make the password
tempPass = []

#Select some lowers
 ##ASCII lowers 97-122
 ##ASCII uppers 65-90

#amount of each
symbolsNo = int(size/3)
lowersNo = size-(symbolsNo)
uppersNo = size-lowersNo

for i in range(lowersNo):
    tempPass.append(chr(randint(97,122)))

for i in range(uppersNo):
    tempPass.append(chr(randint(65,90)))

for i in range(symbolsNo):
    tempPass.append(symbols[randint(0, len(symbols))])

shuffle(tempPass)

print(f'Your password is: {"".join(tempPass)}')





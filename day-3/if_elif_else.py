print('enter your percentage obtained')
percentage = int(input())
if percentage >=0 and percentage <= 100:
    print('your percentage obtained is ' + str(percentage))

if percentage >= 0 and percentage < 40:
    print('you failed')
elif percentage >= 40 and percentage < 50:
    print('3rd division')
elif percentage >= 50 and percentage < 60:
    print('2nd division')
elif percentage >= 60 and percentage < 80:
    print('1st division')
elif percentage >= 80 and percentage <= 100:
    print('Distinction')
else:
    print('enter valid input')
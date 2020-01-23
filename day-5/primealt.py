num = int(input('Enter a number \n8'))

for i in range(2,num):
    if num % i == 0  and num != i:
        print ('not prime')
        exit()
print ('prime')
exit()
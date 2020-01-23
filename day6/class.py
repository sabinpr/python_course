num = 876543241321855257
count = 0
# for x in str(num):
#     print(x)
#     break

for i in str(num):
    count = count + 1
# print (i)

string = str(num)
# first = string[0]
# last = string[-1]

# print (first , last)
ss=''
for i in range(1,count-1):
    ss=ss+string[i]
print (ss)
x=count
for i in range(0,count):
    ss=ss+string[x]
    x=x-1
print(ss)

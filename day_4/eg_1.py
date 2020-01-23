current = ['sabin' , 'aditya' , 'rajan' ,'rabin' , 'sanjay']
new = ['sabin' , 'ram' , 'rabin']

for ne in new:
    if ne in current:
        print (ne , ' already exists')

    else:
        print (ne , ' registered')
        current.append(ne)
    
        

print(current)
print(new)


for even_num in range (2,11,2):
    print(even_num )
    print(even_num**2)

even_nums = list(range(2,11,2))
print(even_nums)

list_of_sq = []
for num in even_nums:
    list_of_sq.append(num**2)

print(list_of_sq)


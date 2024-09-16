z = 'abcaabbxxi'
temp = []
for c in z:            # in operater works bloean if already exist check next car
    if c not in temp:
        temp.append(c)
print(temp)
result =''.join(temp)
print(result)




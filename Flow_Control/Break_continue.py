lst = [1,2,4,7,5,8]
for y in lst:
    if (y==5):
        break
    print(y)


print("#################")


#  Here continue statement used and also skip 3 

x = range(1, 20)
for i in x:
    if (i%3==0):
        continue
    print(i)
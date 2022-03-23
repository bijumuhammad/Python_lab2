a=[1,2,3,4,5]
c=[]

for x in a:
    j=x+1
    for j in a:
        c.append(j)
print(c)
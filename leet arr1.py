List=[int(x) for x in input().split()]
l=[]
for i in List:
if i not in l:
    l.append(i)
print(len(l))
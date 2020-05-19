s=input()
s1=[]
for i in s:
    if s.count(i)==1:
        s1.append(i)
print(s.index(s1[0]))
from itertools import combinations
l=[int(x) for x in input().split()]
k=int(input())
s=[]
m=[]
ans=[]
a=list(combinations(l,2))
sums=[]
for i in a:
    sums.append(sum(i))
for i in sums:
    if(i==k):
        s.append(a[sums.index(i)])
for i in s:
    for j in i:
        m.append(j)
for i in m:
    if i in l:
        ans.append(l.index(i))
print(ans)
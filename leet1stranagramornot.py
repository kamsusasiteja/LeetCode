from itertools import permutations
s=input()
t=input()
l=list(permutations(s))
perms=[]
# string=""
for i in l:
    string=""
    for j in i:
        string=string+j
    perms.append(string)
if t in perms:
    print("True")
else:
    print("False")
  
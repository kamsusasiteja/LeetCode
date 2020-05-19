s=input()
flag=0
s = "".join([f for f in s.lower() if f.isalnum()])
for l,r in zip(s,s[::-1]):
    if l != r:
        flag=1
        break
    else:
        flag=0
if flag==1:
    print("not palin")
else:
    print("palin")
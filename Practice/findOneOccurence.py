li=[3,3,3,9,9,9,18,18,18,21,30,30,30]

def check(ele,i):
    x=t-(ele*5)


count=0
ele=None
t=sum(li)
for i in li:
    if (t-i)%3!=0:
        continue
    else:
        if count==0:
            ele=i
        
        count+=1

        if count==2:
            check()

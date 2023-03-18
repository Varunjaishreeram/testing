s,D=72,9
i=D
result=0
Diff=(9)*D-s
while(i>=1):
    if Diff<9:
        temp=9-Diff
        temp=temp*(10**(i-1))
        result+=temp
        # print(temp,result)
        Diff-=Diff
    else:
        if i==D:
            temp=9-8
            temp=temp*(10**(i-1))
            result+=temp
            Diff-=8
        else:
            temp=9-9
            temp=temp*(10**(i-1))
            result+=temp
            Diff-=9
    i-=1

print(result)

# val=result//10
# prev=result%10
# i=2
# D=7
# while(i<=D):
    
#     currentDigit=val%10
    
#     if currentDigit<9 and (prev//(10**(i-2)))!=0:
        
#         val+=1
#         prev=prev-(10**(i-2))
#         val=val*(10**(i-1))
#         result=val+prev
#         break


#     t=10**(i-1)
#     prev=(currentDigit*t)+prev
#     val=val//10

#     i+=1

val=str(result)
for i in range(D-2,-1,-1):
    if int(val[i])<9 and int(val[i]!=0):
        result=""
        result+=val[0:i]
        result+=str(int(val[i])+1)
        result+=str(int(val[i+1])-1)
        result+=val[i+2:]
        break


result=int(result)

print(result)







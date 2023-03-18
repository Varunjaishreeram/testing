arr=[1,2,3,7,5]
val=12
currentSum=0
i=0
start=i
flag=0
while(i<len(arr)):
    currentSum+=arr[i]
    while currentSum>val and start<i:
        currentSum-=arr[start]
        start+=1
    
    if currentSum==val:
        flag=1
        break

    i+=1

if flag:
    print("yes",start,i)

else:
    print("no")
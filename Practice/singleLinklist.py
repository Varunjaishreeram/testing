class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None


class SLink:
    def __init__(self) -> None:
        self.head=None
        self.tail=None

    def add(self,value,location="l"):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode

        #adding the node in the starting
        elif location=="s":
            newNode.next=self.head
            self.head=newNode

        # adding node in the last
        elif location=="l":
            newNode.next=None
            self.tail.next=newNode
            self.tail=newNode
        
        else:
            prevNode=self.head
            index=0
            while index<(location-1):
                prevNode=prevNode.next
                index+=1
            
            if index==0:
                
                newNode.next=prevNode
                prevNode=newNode
                # self.head=prevNode
                
            else:
                newNode.next=prevNode.next
                prevNode.next=newNode

    
    def printSL(self):
        print("[",end="")
        while self.head.next!=None:
            print(f" {self.head.value},",end="")
            self.head=self.head.next
        
        print(f" {self.head.value}",end=" ")
        print("]")

singleLink=SLink()
singleLink.add(1)
singleLink.add(2)
singleLink.add(3,0)
singleLink.add(-1,0)
singleLink.add(4,0)
singleLink.printSL()

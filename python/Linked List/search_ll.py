/**
@file
@breif this is general implementation of linked list with search operation
**/
/**
linked-list class has five methods and one constructer including insert-node,deleteing first node,deleting last node,searching an element in list and veiwing whole linked list
**/

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None
    def insert_node(self,value):
        newnode=node(value)
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
        return self.head

    def deleteFirst(self):
        if self.head==None:
            print("linked list is empty")
        else:
            self.head=self.head.next
        return self.head

    def deletelast(self):
        if self.head == None:
            print("linked list is empty")
        else:
            temp = self.head
            while temp.next!=None:
                x=temp
                temp=temp.next
            x.next=None
        return self.head
    def search(self,data):
        flag=0
        temp=self.head
        while temp!=None:
            if temp.data==data:
                flag=1
                break
            temp=temp.next
        if flag==1:
            return True
        else:
            return False

    def viewll(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next


if __name__=="__main__":
    n = int(input("Enter number of node you need:"))
    Node = linked_list()
    while n>0:
        x = int(input())
        ll=Node.insert_node(x)
        n-=1
    Node.deleteFirst()
    Node.deletelast()
    d=int(input("Enter element you want to delete: "))
    if Node.search(d)==True:
        print("Element is present")
    else:
        print("Element not present!")
    Node.viewll()



class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def insert_at(self,index,data):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid index")
        if index==0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
    def insert_at_begining(self,data):    
        node= Node(data,self.head)
        self.head=node
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def remove_at(self,index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break

            itr=itr.next
            count+=1

    def getLength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def print(self):
        if self.head is None:
            print("List is empty")
            return
        itr=self.head
        strs=''
        while itr:
            strs+=str(itr.data)+'->'
            itr=itr.next
        print(strs,end="")
        print("null")
if __name__=='__main__':
    liste=LinkedList()
    liste.insert_values([13,22,54,67])
    liste.remove_at(3)
    liste.insert_at(2,7)
    liste.print()
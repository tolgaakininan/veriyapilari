class Node:
    def __init__(self,data=None,next=None,previous=None) -> None:
        self.data=data
        self.next=next
        self.previous=previous
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
    def insert_value_after_data(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data==data_after:
            self.head.next=Node(data_to_insert,self.head.next)
            return
        itr=self.head
        while itr:
            if itr.data==data_after:
                itr.next=Node(data_to_insert,itr.next)
                break
            itr=itr.next
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

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
    def removeByValue(self,data):
        if self.head is None:
            return
        if self.head.data ==data:
            self.head=self.head.next
        else:
            itr=self.head
            while itr:
                
                if itr.next.data==data:
                    itr.next=itr.next.next
                    break
                itr=itr.next
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
    liste.insert_at(2,7)
    liste.removeByValue(13)
    liste.insert_value_after_data(22,50)
    liste.print()

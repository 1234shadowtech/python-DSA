#part1



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linked_list:
    def __init__(self):
        self.head=None
        
    def add_node(self):
        n=int(input("enter the no of node to add"))
        for i in range n:
            self.data=input("enter the data")
            new_node=Node(self.data)
            if not self.head:
                self.head =new_node
            else:
                current=self.head
                while current.next:
                    current=current.next
                current.next=new_node
            
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        print("none")
        
ll=linked_list()
ll.add_node()
ll.display()
class linked_list:
    def __init__(self):
        self.a=[]
    def create_list(self):
        q=int(input("enter the number of elements in the list"))
        for i in range(q):
            b=int(input("enter the element"))
            self.a.append(b)
        print(self.a)
    def insrt_elm(self):
        e=int(input("enter the number of elemnts to be inserted into list"))
        for i in range (e):
            c=int(input("enter the number to be inserted into the list"))
            d=int(input("enter the position in which the number to be added into the list"))
            self.a.insert(d,c)
        print(self.a)
    def del_elm(self):
        f=int(input("enter the no of elments to delete from the list"))
        for i in range(f):
            g=int(input("enter the element to be deleted "))
            self.a.remove(g)
        print(self.a)
    def change_value(self):
        h=int(input("enter the number you need add into the list"))
        j=int(input("enter the position of the value you need to change"))
        if 0<=j<len(self.a):
            self.a[j]=h
            print(self.a)
        else:
            print("wrong input")
    def fetch_elm(self):
        k=int(input("ener the index of the element to be fetched"))
        if 0<=k<len(self.a):
            print(self.a[k])
        else:
            print("invaled index value") 
    def reverse_list(self):
        rev_a=self.a[::-1]
        print(rev_a) # the reverse can also be done by 
        # self.a.reverse()
        #print(self.a)

    def display(self):
        print("basic operations on python\nchoose the operatin you would like to perform") 
        print("1.create\n 2.inest\n 3.delete\n 4.change\n 5.fetch\n 6.reverse")
        s=int(input("enter the no of the option you chosed "))
        lc.switch_case(s)
# 
    def switch_case(self,m):
        if m==1:
            lc.create_list()
            lc.display()
        elif m==2:
            lc.insrt_elm()
            lc.display()
        elif m==3:
            lc.del_elm()
            lc.display()
        elif m==4:
            lc.change_value()
            lc.display()
        elif m==5:
            lc.fetch_elm()
            lc.display()
        elif m==6:
            lc.reverse_list()
            lc.display()
        else:
            print("wrong input")
            lc.display()
lc=linked_list()
lc.display()


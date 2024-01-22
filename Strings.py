#part1
class string1:
    def __init__(self):
        self.a=""
        self.b=""
    def create_string(self):
        self.a=str(input("enter the first desired string"))
        self.b=str(input("enter the second desired string"))
        print(self.a)
        print(self.b)
        
    def merge_string(self):
        c=self.a+self.b
        print(c)
    
    def sub_sting(self):
        index1=int(input("enter the starting index of the substring"))
        index2=int(input("enter the final index of the sub string"))
        substring = self.a[index1:index2]
        print(substring)    
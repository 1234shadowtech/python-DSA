def calculator():
    num1=int(input("enter the number1"))
    num2=int(input("enter the number 2"))
    print("1:addtion\n2:subtraction\n3:multiplication\n4:division")
    op=int(input("enter the opertion number"))
    if  op==1:
        print("the result  of addition is",num1+num2)
    elif op==2:
        print("the result of subtraction is ",num1-num2)
    elif op==3:
        print("the result of multiplication is",num1*num2)
    elif op==4:
        if num2!=0 :
            print("the result of division is",num1/num2)
    else:
        print("wromg input ")
calculator()
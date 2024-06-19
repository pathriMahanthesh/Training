def sum(a,b):
    return a+b
c=sum(98,90)
print(c)

#even odd
num=1
if num<0:
    print("invalid")
elif num>0:
    if num%2==0:
        print("even")
    else:
        print("odd")

#positional arguements:
def sum(a,b):
    return a+b
print(sum(4,6))
#default arguments
def sum(a,b=90):
    return a+b
print(sum(6))
#Keyword arguments:
def sum(a,b):
    return a+b
print(sum(a=12,b=13))
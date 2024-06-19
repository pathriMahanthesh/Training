#1. positional argument
def sumOfNumbers(a,b):
    print(a)
    print(b)
    return a+b
c=sumOfNumbers(18,20)
print(c)

#2. default argument
def myself(name,age):
    print(name)
    print(age)
    return None
myself("sri",age=24)

#3. key word argument:
def goodMorning(name,age):
    print(name)
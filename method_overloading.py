class Calculator:
    intro="hey....in class variable"
    def add(self, *args):
        total=0
        for i in args:
            total=total+i
        return total
    
#reate an instancce of the calculator class       
calculator=Calculator()

#call the overloaded add methods
print(calculator.add(2,3))
print(calculator.add(2,3,4))
print(calculator.add(2,3,4,5))
print(calculator.add(2,3,4,5,6))
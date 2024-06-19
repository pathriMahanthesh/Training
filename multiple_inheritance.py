class father:
    def parent_method():
        return "is the father"
class mother:
    def parent_method():
        return "is the mother"
class child:
    def child_method():
        return "is the child"
obj1=father
obj2=mother
print(obj1.parent_method())
print(obj2.parent_method())    
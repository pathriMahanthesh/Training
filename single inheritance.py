#1. single inheritance
class parent:
    def parent_method():
        return "im parent method"
class child(parent):
    def child_method():
        return "im child method, derived from parent method"

obj1=child
print(obj1.child_method())
print(obj1.parent_method())
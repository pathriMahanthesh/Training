set1={1,2,3,4,5}
set2={6,7,8,9}
print(*set1)
print(*set2)
set1=set1.union(set2)
print(*set1)
set=set1.intersection(set2)
print(*set)
set3=set1.difference(set2)
print(*set3)
set4=set1.symmetric_difference(set2)
set4.remove(5)
print(*set4)
print(set1.discard(3))
print(set1.pop())
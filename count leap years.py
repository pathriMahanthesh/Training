count=0
for i in range(1850,2025):
    if i%400==0 or (i%100!=0 and i%4==0):
        count+=1

print(count)
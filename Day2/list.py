cars=[1,2,3,"surjeet","verma"]
print(type(cars))
print(len(cars))
cars.append("123")
cars.append([1,2,3])
print(cars)

cars[::-1]#to reverse
#l.sort(),pop,insert,sorted,max(l),min(l),sum(l),
print(cars)
# a is b means id(a)==id(b)
print(list(map(int,[1,2,3,"123"])))

cin=list(map(int,input().split()))

print(cin)
#------------------DEQUE-------------------


from collections import deque
a=deque([10,11,12])
print(a)

print(a[1])

a.append(13)
print(a)

a.appendleft(65)
print(a)

a.append("alan")
print(a)

a.extend(["tr"])
print(a)

a.extendleft(["andanother"])
print(a)

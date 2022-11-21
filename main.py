from mylist import *

l = [1,2,3]
obj = listfunctions(l)

print(f"Instance before append: {obj.l}")
obj.append([5,6,7])
print(f"Instance after append: {obj.l}")

print("---------------------------------")
e = ["lo", 2, 5]

print(f"Instance before extend: {obj.l}")
obj.extend(e)
print(f"Instance after append: {obj.l}")

print("---------------------------------")

print(f"Instance before insert: {obj.l}")
obj.insert(0, "abhijit")
print(f"Instance after insert: {obj.l}")

print("---------------------------------")

print(f"Instance before insert: {obj.l}")
obj.insert(5, "abhijit")
print(f"Instance after insert: {obj.l}")

print("---------------------------------")

print(f"Instance before insert: {obj.l}")
obj.insert(100, "abhijit")
print(f"Instance after insert: {obj.l}")

print("---------------------------------")

print(f"Instance before remove: {obj.l}")
obj.remove("abhijit")
print(f"Instance after remove: {obj.l}")

print("---------------------------------")

print(f"Instance before pop: {obj.l}")
obj.pop(5)
print(f"Instance after pop: {obj.l}")

print("---------------------------------")

print(f"Index of '3' in the list is: {obj.l.index(3)}")

print("---------------------------------")

ob1 = listfunctions([3, 9.4, 7, 3.2, 0])
print(f"Instance before sort: {ob1.l}")
ob1.sort()
print(f"Instance after sort: {ob1.l}")

print("---------------------------------")

ob2 = listfunctions(['Cab', 'ab', 'rt', 'op', 'ac', 'Cac'])
print(f"Instance before sort: {ob2.l}")
ob2.sort()
print(f"Instance after sort: {ob2.l}")

print("---------------------------------")

print(f"Instance before clear: {ob1.l}")
ob1.clear()
print(f"Instance after clear: {ob1.l}")

print("---------------------------------")

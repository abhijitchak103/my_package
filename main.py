from mylist import *

l = [1,2,3]
obj = listfunctions(l)

print(f"Instance before append: {obj.l}")
obj.myappend([5,6,7])
print(f"Instance after append: {obj.l}")

print("---------------------------------")
e = ["lo", 2, 5]

print(f"Instance before extend: {obj.l}")
obj.myextend(e)
print(f"Instance after append: {obj.l}")

print("---------------------------------")

print(f"Instance before insert: {obj.l}")
obj.myinsert(0, "abhijit")
print(f"Instance after insert: {obj.l}")

print("---------------------------------")

print(f"Instance before insert: {obj.l}")
obj.myinsert(5, "abhijit")
print(f"Instance after insert: {obj.l}")

print("---------------------------------")

print(f"Instance before insert: {obj.l}")
obj.myinsert(100, "abhijit")
print(f"Instance after insert: {obj.l}")

print("---------------------------------")
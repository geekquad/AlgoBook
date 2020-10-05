
a = set()
b = set()

m = int(input("Enter number elements in set 1: "))
n = int(input("Enter number elements in set 2: "))

print("Enter elements of set 1: ")
for i in range(m):
    a.add(input())

print("Enter elements of set 2: ")
for i in range(n):
    b.add(input())

similarity = len(a.intersection(b))/len(a.union(b))
print("Similarity index: {} ".format(similarity))
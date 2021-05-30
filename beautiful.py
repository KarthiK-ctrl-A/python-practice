li = [int(item) for item in input("Enter the list items : ").split()]
tup = tuple(li)
n = tup[0]
x = len(tup)
ll = []
for i in tup:
    if (tup[i]%n==0):
        ll.append(tup[i])
if (len(ll)==x):
    print("YES")
else:
    print("no")
    
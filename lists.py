li = []
n = int(input())
for i in range(n):
    a = input().split()
    for j in range(1,len(a)):
        a[j] = int(a[j])
    
    if a[0] == "append":
        li.append(a[1])
    elif a[0] == "insert":
        li.insert(a[1],a[2])
    elif a[0] == "remove":
        li.remove(a[1])
    elif a[0] == "pop":
        li.pop()
    elif a[0] == "sort":
        li.sort()
    elif a[0] == "reverse":
        li.reverse()
    elif a[0] == "print":
        print(li)
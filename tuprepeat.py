N = int(input())
T = int(input())
M = int(input())
li = []
for i in range(0,M):
    for j in range(0,M-T):
         li.append(T)
    T += 1

lst1 = li[0:T]
lst2 = li[T:]
tup1 = tuple(lst1)
tup2 = tuple(lst2)
tup = str(tup1)+str(tup2)
print(str(tup))
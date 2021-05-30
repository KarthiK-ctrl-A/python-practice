N = int(input()) #number of elements
start = int(input()) #number
end = int(input()) #condition
li =[]
for i in range(0,end):
    for j in range(0,end-start):
        li.append(start)
    start += 1
print(li)

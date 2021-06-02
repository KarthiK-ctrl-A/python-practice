first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

if(n%2!=0 and m==n*3):
    for i in range (1,n,2):
        print((".|."*i).center(m,'-'))
    
    print(("WELCOME").center(m,'-'))

    for i in range(n-2,-1,-2):
        print((".|."*i).center(m,'-'))

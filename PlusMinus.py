#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.

#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

#Example

#There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

#0.400000
#0.400000
#0.200000
pos = 0
neg = 0
zero = 0
n = int(input("Enter the size of the array"))
li = []
for i in range(0, n):
    print("Enter Element {}".format(i+1))
    ele = int(input())
    li.append(ele)
for num in li:
    if num>=0:
        if num==0:
            zero += 1
        else:
            pos += 1
    else:
        neg += 1

pos = pos/n
neg = neg/n
zero = zero/n
print('%.4f'%pos)
print('%.4f'%neg)
print('%.4f'%zero)
if __name__ == '__main__':
    li = []
    dic = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score] = [name]
        if score not in li:
            li.append(score)

    l = min(li)
    li.remove(l)
    sl = min(li)
    dic[sl].sort()
    for i in dic[sl]:
        print(i)


        
x, y = map(int, input().split())

x_list = []
y_list = []
count = 2


def rec_1(x_y, cnt, lst):
    if x_y % cnt == 0:
        p = x_y // cnt
        if p != 1:
            lst.append(cnt)
            rec_1(p, cnt, lst)
        if p == 1:
            lst.append(x_y)
            return lst

    if x_y % cnt != 0:
        cnt += 1
        rec_1(x_y, cnt, lst)

    return lst

def nok(x_r, y_r):
    data = []
    for i in x_r:
        data.append(i)
        for j in y_r:
            if j not in data:
                data.append(j)
    return data





s = rec_1(x, count, x_list)
print(s)
d = rec_1(y, count, y_list)
print(d)

print(nok(s, d))


# if y % x != 0:
#     print(0)
# else:
#     rec_1(x)

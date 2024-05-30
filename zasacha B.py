from math import prod

x, y = map(int, input('2 числа через пробел: ').split())


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


def nok(x_k, y_k):
    data = []
    for i in x_k:
        data.append(i)
    for j in y_k:
        if j not in data:
            data.append(j)
        data.sort()
    result = prod(data)

    return result


def nod(x_d, y_d):
    if y_d == 0:
        return x_d
    else:
        return nod(y_d, x_d % y_d)


s = rec_1(x, count, x_list)

d = rec_1(y, count, y_list)


print(nod(x, y))
print(nok(s, d))



from math import prod
x, y = map(int, input('2 числа через пробел: ').split())


def res_1(nod_x, nok_y):
    x_y = nod_x * nok_y
    data_1 = {}
    lst = []
    count_1 = 0

    for i in range(1, x_y+1):
        if x_y % i == 0:
            lst.append(i)
            for j in lst:
                res = x_y // j

                data_1[j] = [j, res]

    lst.clear()
    for value in data_1.values():
        if value[0] % nod_x == 0 and value[1] % nod_x == 0:
            lst.append(value)
            count_1 += 1

    return (f'всего {count_1} вариант(ов) закрытых ключей (p,q), таких, '
            f'что открытым ключом для них является {(x, y)}: {lst}')




print(res_1(x, y))






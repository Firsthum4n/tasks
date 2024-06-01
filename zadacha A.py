import math

input_1 = ('2 '
           'sandwich 7 3 '
           'butter 10 g '
           'toasted_bread 2 cnt '
           'sausage 30 g '
           'omelet 9 4 '
           'egg 4 cnt '
           'milk 120 ml '
           'salt 1 g '
           'sausage 50 g '
           '7 '
           'egg 61 1 tens '
           'milk 58 1 l '
           'sausage 100 480 g '
           'butter 120 180 g '
           'cream 100 350 g '
           'salt 14 1000 g '
           'toasted_bread 40 20 cnt '
           '8 '
           'egg 1 cnt 13 12 1 16.4 '
           'milk 1 l 3 4.5 4.7 60 '
           'chocolate 90 g 6.8 36.3 47.1 546 '
           'salt 1 kg 0 0 0 0 '
           'strawberry 100 g 0.4 0.1 7 35 '
           'sausage 100 g 10 18 1.5 210 '
           'toasted_bread 5 cnt 7.3 1.6 52.3 248 '
           'butter 100 g 0.8 72.5 1.3 661')

dish_dict = {}
list_of_dish = []

count = int(input_1[0])


def read_dish(input_str, cnt):
    split_input = input_str.split()
    dish = split_input[0]
    len_ingredient = int(split_input[2]) * 3
    if dish not in dish_dict:
        quantity = []
        lst = []
        quantity.append(split_input[1])

        for i in range(len_ingredient):
            lst.append(split_input[3:][i])

        dish_dict[dish] = (quantity, lst)

    cnt -= 1
    next_level = ' '.join(split_input[3 + len_ingredient:])

    if cnt > 0:
        return read_dish(next_level, cnt)
    else:
        return next_level


def append_dish_to_list():
    for dish_key in dish_dict.keys():
        dish_quantity = ''.join(dish_dict[dish_key][0])
        dish_key = Dish(dish_key, int(dish_quantity), dish_dict[dish_key][1])
        list_of_dish.append(dish_key)


def sum_dct():
    ingredients_1 = list_of_dish[0].get_ingredients()
    ingredients_2 = list_of_dish[1].get_ingredients()
    for key, values in ingredients_1.items():
        for key_1, values_1 in ingredients_2.items():
            if key == key_1:
                ingredients_1[key] = [values[0] + values_1[0], values[1]]
    sum_dict = ingredients_2 | ingredients_1
    return sum_dict


def price(combined_ingredients, price_list):
    total_price = 0
    pars_dict = {}
    result_dict = {}
    count_3 = 0
    split_price_list = price_list.split()
    list_prices = price_list.split()[1:]
    for i in range(int(split_price_list[0])):
        pars_dict[list_prices[i + count_3]] = [list_prices[i + 1 + count_3], int(list_prices[i + 2 + count_3]),
                                               list_prices[i + 3 + count_3]]
        count_3 += 3
    for key, value in combined_ingredients.items():
        for key_p, value_p in pars_dict.items():
            if key == key_p and value[1] == value_p[2] and value[0] <= value_p[1]:
                result_dict[key] = 1
                total_price += int(value_p[0])
            elif key == key_p and (value[1] == 'cnt' and value_p[2] == 'tens'):
                value_p[1] *= 10
                if key == key_p and value[0] <= value_p[1]:
                    result_dict[key] = 1
                    total_price += int(value_p[0])
                elif key == key_p and value[0] > value_p[1]:
                    cnt = 1
                    intermediate = value_p[1]
                    while value[0] > value_p[1]:
                        value_p[1] += intermediate
                        cnt += 1
                    result_dict[key] = cnt
                    total_price += (int(value_p[0]) * cnt)
            elif key == key_p and (value[1] == 'ml' and value_p[2] == 'l'):
                value_p[1] *= 1000
                if key == key_p and value[0] <= value_p[1]:
                    result_dict[key] = 1
                    total_price += int(value_p[0])
                elif key == key_p and value[0] > value_p[1]:
                    cnt = 1
                    intermediate = value_p[1]
                    while value[0] > value_p[1]:
                        value_p[1] += intermediate
                        cnt += 1
                    result_dict[key] = cnt
                    total_price += (int(value_p[0]) * cnt)
            elif key == key_p and value[1] == value_p[2] and value[0] > value_p[1]:
                cnt = 1
                intermediate = value_p[1]
                while value[0] > value_p[1]:
                    value_p[1] += intermediate
                    cnt += 1
                result_dict[key] = cnt
                total_price += (int(value_p[0]) * cnt)
    pars_result_dict = {total_price: ''}
    for key, value in result_dict.items():
        pars_result_dict[key] = value
    return pars_result_dict


def energy_value(pars_dct, result1):
    data_dict = {}
    count_4 = 0
    for i in range(len(result1) + 1):
        data_dict[pars_dct[0+count_4]] = [pars_dct[1+count_4], pars_dct[2+count_4], pars_dct[3+count_4],
                                          pars_dct[4+count_4], pars_dct[6+count_4], pars_dct[6+count_4]]
        count_4 += 7
    print(data_dict)
    sandwich = list_of_dish[0].ingredients
    omlet = list_of_dish[1].ingredients





class Dish:
    def __init__(self, name, quantity, ingredients):
        self.name = name
        self.quantity = quantity
        self.ingredients = ingredients

    def print_info(self):
        print(f'{self.name}, {self.quantity}, {self.ingredients}')

    def get_ingredients(self):
        dict_of_ingredients = {}
        count_2 = 0
        for i in range(len(self.ingredients) // 3):
            ingredient_r = ''.join(self.ingredients[i + 1 + count_2])
            dict_of_ingredients[self.ingredients[i + count_2]] = [int(ingredient_r) * self.quantity,
                                                                  self.ingredients[i + 2 + count_2]]
            count_2 += 2
        return dict_of_ingredients


def main():
    to_next = read_dish(input_1[1:], count)
    append_dish_to_list()
    summ = sum_dct()
    result_1 = price(summ, to_next)
    len_next = int(to_next.split()[0]) * 4
    to_next_2 = to_next.split()[len_next + 1:]
    # print(to_next_2)
    # for key, value in result_1.items():
    #     print(key, value)

    print(list_of_dish[1].ingredients)


if __name__ == '__main__':
   main()

from pprint import pprint

cook_book = {}

with open('recipes.txt','r', encoding='utf-8') as file:
    for line in file:
        if (not("|" in line)) and not(line[:-1].isnumeric()) and len(line) > 1:
            list = []
            cook_book.setdefault(line[:-1])
            key = line[:-1]
        elif "|" in line:
            new_line = line.split(' | ')
            dict = {}
            dict['ingredient_name'] = new_line[0]
            dict['quantity'] = int(new_line[1])
            dict['measure'] = new_line[2][:-1]
            list.append(dict)
        else:
            pass
        cook_book[key] = list
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            dict_shop_list = {}
            a = shop_list.setdefault(ingredient['ingredient_name'],dict_shop_list)
            if a != {}:
                a['quantity'] += ingredient['quantity']*person_count
            else:
                dict_shop_list['quantity'] = ingredient['quantity']*person_count
            
            dict_shop_list['measure'] = ingredient['measure']
            
    pprint(shop_list)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
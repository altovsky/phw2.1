# -*- coding: utf-8 -*-

from pprint import pprint


def read_cook_book(cook_book_path):
    cook_book = dict()
    with open(cook_book_path, mode='r', encoding='utf-8') as db:
        while True:
            dish = db.readline().strip()
            cook_book[dish] = []

            number_of_ingredients = db.readline().strip()
            for iteration in range(int(number_of_ingredients)):
                ingridient_record = db.readline().strip()
                ingridient_data = ingridient_record.split(' | ')

                cook_book[dish].append(
                    {
                        'ingridient_name': ingridient_data[0],
                        'quantity': int(ingridient_data[1]),
                        'measure': ingridient_data[2]
                    }
                )

            separator = db.readline()
            if not separator:
                break

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book_file_path):
    cook_book_db = read_cook_book(cook_book_file_path)
    shop_list_by_dishes = {}

    for dish in dishes:
        for ingredient in cook_book_db[dish]:
            ingridient_name = ingredient['ingridient_name']
            if ingridient_name in shop_list_by_dishes:
                shop_list_by_dishes[ingridient_name]['quantity'] += ingredient['quantity'] * person_count
            else:
                shop_list_by_dishes[ingridient_name] = {
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * person_count
                    }

    return shop_list_by_dishes


pprint(get_shop_list_by_dishes(
    ['Фахитос', 'Запеченный картофель', 'Омлет'], 3, 'dz2.1.txt')
       )

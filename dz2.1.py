# -*- coding: utf-8 -*-

from pprint import pprint


def count_file_lines(file_path):
    fl = open(file_path, mode='r', encoding='utf-8')
    file_lines_number = len(fl.readlines())
    fl.close()
    return file_lines_number


def read_cook_book(cook_book_path):
    cb_lines_number = count_file_lines(cook_book_path)
    cook_book = dict()
    with open(cook_book_path, mode='r', encoding='utf-8') as db:
        current_line = 0  # Счетчик прочитанных строк
        while True:
            dish = db.readline()
            cook_book[dish.strip()] = current_line
            current_line += 1
            # Далее не будем использовать, встроенный в данные счетчик ингридиентов. Посчитаем сами.
            number_of_ingredients = db.readline()
            current_line += 1
            cook_book[dish.strip()] = []

            while True:
                ingridient_record = db.readline()
                ingridient_record = ingridient_record.strip()
                current_line += 1
                if ingridient_record == '':  # Если конец "секции"
                    break
                else:
                    ingridient_data = ingridient_record.split(' | ')
                    cook_book[dish.strip()].append(
                        {
                            'ingridient_name': ingridient_data[0],
                            'quantity': int(ingridient_data[1]),
                            'measure': ingridient_data[2]
                        }
                    )

            if current_line > cb_lines_number:  # Если последняя строка в файле
                break

    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book_file_path):
    cook_book_db = read_cook_book(cook_book_file_path)
    shop_list_by_dishes = {}

    for i in dishes:
        for ii in range(len(cook_book_db[i])):
            ingridient_name = cook_book_db[i][ii]['ingridient_name']
            if ingridient_name in shop_list_by_dishes:
                shop_list_by_dishes[ingridient_name]['quantity'] += \
                    cook_book_db[i][ii]['quantity'] * person_count
            else:
                shop_list_by_dishes[ingridient_name] = {
                    'measure': cook_book_db[i][ii]['measure'],
                    'quantity': cook_book_db[i][ii]['quantity'] * person_count
                    }

    return shop_list_by_dishes


pprint(get_shop_list_by_dishes(
    ['Фахитос', 'Запеченный картофель', 'Омлет'], 3, 'dz2.1.txt')
       )

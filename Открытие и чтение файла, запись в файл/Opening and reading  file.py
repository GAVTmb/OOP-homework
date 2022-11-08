with open('recipes.txt', encoding='utf-8') as recept:
    cook_book = {}
    for line in recept:
        name_dish = line.strip().lower()
        number_ingredients = int(recept.readline())
        ingredients_dish = []
        for _ in range(number_ingredients):
            ingredients = recept.readline().strip().split(' | ')
            product_name, quantity, unit_of_meas = ingredients
            ingredients_dish.append({'product_name': product_name,
                                     'quantity': int(quantity),
                                     'unit_of_meas': unit_of_meas})
        recept.readline()
        cook_book[name_dish] = ingredients_dish


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            ingridient['quantity'] *= person_count
            if ingridient['product_name'] not in shop_list:
                shop_list[ingridient['product_name']] = ingridient
            else:
                shop_list[ingridient['product_name']]['quantity'] += ingridient['quantity']
    return shop_list


def print_shop_list(shop_list, person_count, dishes):
    print(f'Продукты для блюд(а): "{", ".join(list(dishes)).title()}" на {person_count} человек(а):')
    for shop_list_item in shop_list.values():
        print(shop_list_item['product_name'], shop_list_item['quantity'],
              shop_list_item['unit_of_meas'])


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    print(f'Список блюд: "{", ".join(list(cook_book.keys())).title()}"')
    dishes = input('Введите блюда (через запятую): ').lower().split(', ')
    for dishe in dishes:
        if dishe not in cook_book.keys():
            return print('Нет такого блюда!')

        else:
            ...
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list, person_count, dishes)


create_shop_list()

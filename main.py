with open('recept.txt', encoding='utf-8') as file:
    # res = file.readlines()
    # print(res)
    cook_book = {}

    for line in file:
        # file.seek(0)
        dish = line.strip()
        quantity_ingredients = int(file.readline())
        # print(dish)
        ingredients = []
        for i in range(quantity_ingredients):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        cook_book[dish] = ingredients
        file.readline()
# print(cook_book)

ing = {}


def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        for i in cook_book.get(dish):
            a = i['ingredient_name']
            b = {'quantity': int(i['quantity']) * person_count,'measure': i['measure']}
            ing[a] = b
    print(ing)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
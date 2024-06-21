def read_recipes():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as f:
        recipes = []
        current_recipe = []
        for line in f:
            line = line.strip()
            if line:
                current_recipe.append(line)
            else:
                recipes.append(current_recipe)
                current_recipe = []

        if current_recipe:
            recipes.append(current_recipe)

        for recipe in recipes:
            dish = recipe[0]
            quantity = int(recipe[1])

            ingredients = []
            for i in range(2, quantity + 2):
                ingredient_name, quantity, measure = recipe[i].split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure})

            cook_book[dish] = ingredients

    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    foods = {}
    for dish in dishes:
        ingredients_for_dish = cook_book[dish]
        for ingredient in ingredients_for_dish:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity']
            measure = ingredient['measure']

            if ingredient_name in foods:
                foods[ingredient_name]['quantity'] += quantity
            else:
                foods[ingredient_name] = {'measure': measure, 'quantity': quantity}

    for ingredient_name, data in foods.items():
        data['quantity'] *= person_count

    return foods

def merge_files(file_names):
    sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[1])

    with open('result.txt', 'w', encoding='utf-8') as result_file:
        for file_name, line_count in sorted_file_data:
            file_content = open(file_name, encoding='utf-8').read()
            result_file.write(f'Имя файла: {file_name}\n')
            result_file.write(f'Количество строк: {line_count}\n')
            result_file.write(file_content + '\n\n')

cook_book = read_recipes()
dishes = ['Омлет', 'Фахитос']
person_count = 2
shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)
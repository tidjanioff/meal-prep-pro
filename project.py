import random
import sys
from tabulate import tabulate

days = ["", "DAY 1", "DAY 2", "DAY 3", "DAY 4", "DAY 5", "DAY 6", "DAY 7"]
def main():
    welcome()

    while True:
        try:
            users_option = int(input("→ Tap 1 to generate your 7-day menu\n→ Tap 2 if you want to add new meals to the \
collection\n→ Tap 0 to end the program\n$ "))
            allowed_options = [1, 2, 0]
            if users_option in allowed_options:
                break
            print("Please enter 1, 2 or 0", "", sep="\n")
        except ValueError:
            print("Please enter 1, 2 or 0", "", sep="\n")

    if users_option == 0:
        copyright(2)
    elif users_option == 1:
        here_is('menu')

        all_breakfast = meal_generator('breakfast')
        all_lunch = meal_generator('lunch')
        all_dinner = meal_generator('dinner')

        menu = menu_generator(all_breakfast, all_lunch, all_dinner)

        display_table(menu)

        while True:
            try:
                end_check = int(input("→ Tap 3 to display this menu's calorie intake\n→ Tap 4 to generate a groceries \
list for this menu\n→ Tap 5 to search for the ingredients of a recipe\n→ Tap 0 to end the program\n\n$ "))
                if end_check == 0:
                    copyright(2)
                    break
                elif end_check == 3:
                    here_is('calorie intake')
                    calorie_intake_table = calorie_intake_table_maker(all_breakfast, all_lunch, all_dinner)
                    display_table(calorie_intake_table)

                    while True:
                        try:
                            print("Do you want the groceries list for this menu?", "→ Tap 4 if you do", "→ Tap 0 to \
end the program", "", sep="\n")

                            end_check_2 = int(input("$ "))
                            if end_check_2 == 4:
                                here_is('groceries list')
                                final_list_groceries = groceries_list_maker(all_breakfast, all_lunch, all_dinner)
                                print(" ", *final_list_groceries, sep="\n→ ")
                                copyright(1)
                                break
                            elif end_check_2 == 0:
                                copyright(2)
                            break

                        except ValueError:
                            print("Please tap 4 or 0")
                        break
                    break
                elif end_check == 4:
                    here_is('groceries list')
                    final_list_groceries = groceries_list_maker(all_breakfast, all_lunch, all_dinner)
                    print(" ", *final_list_groceries, sep="\n→ ")
                    copyright(1)
                    break
                elif end_check == 5:
                    while True:
                        try:
                            recipe = (input("\nEnter the name of the recipe\n$ ").title().strip())
                            recipe_ingredients = groceries_function(recipe)
                            print(f"\nYou can make your {recipe} if you have : ",*recipe_ingredients,sep="\n→ ")
                            break
                        except TypeError:
                            sys.exit("This recipe is not in our database but you can add it.")
                    copyright(1)
                break
            except ValueError:
                print("Please tap 3, 4, 5 or 0")
            break
    if users_option == 2:
        add_new_meal()



def welcome():
    print("", "This is Meal Prep Pro ", "We help you build a weekly menu and establish your groceries list", "",
          "You have these following options:", "  (1) You can generate a 7-day menu", "  (2) You can add new meals \
on the recipes list", "", "Extra$$:", "   → You can have access to the calorie intake of the generated menu",
          "   → You can ask for a groceries list adapted to the generated menu", "   → You can ask for the ingredients \
of a specific meal", "", "© Meal Prep Pro", "", sep="\n")


def meal_generator(category):
    meals_list_temp = []
    random_meals_list = [f"{category.upper()}"]
    with open(f"{category}.txt", "r") as file:
        for row in file:
            meals_list_temp.append(row.replace("\n", ""))
    for _ in range(7):
        random_meals_list.append(random.choice(meals_list_temp))
    return random_meals_list



def new_meal_writer(meal, category):
    if category == 1:
        with open("breakfast.txt", "a") as file:
            file.write(f"\n{meal}")
    elif category == 2:
        with open("lunch.txt", "a") as file:
            file.write(f"\n{meal}")
    elif category == 3:
        with open("dinner.txt", "a") as file:
            file.write(f"\n{meal}")



def flatten(seq):
    l = []
    for elt in seq:
        t = type(elt)
        if t is tuple or t is list:
            for elt2 in flatten(elt):
                l.append(elt2)
        else:
            l.append(elt)
    return l


def groceries_function(recipe):
    with open("groceries.csv", "r") as file:
        for row in file:
            temp = row.split(",")
            if temp[0] == recipe:
                temp[1] = temp[1].replace('"', "")
                test = temp[1].split(";")
                ingredients = []
                for i in test:
                    ingredients.append(i.strip())
                return ingredients


def calorie(meal):
    with open("calories.csv", "r") as file:
        for row in file:
            line = row.split(";")
            temp = line[0].replace('"', "")
            recipe = meal.title()
            if recipe == temp:
                return line[1].replace("\n", "")

def copyright(option):
    if option == 1:
        print("", "2024 © Meal Prep Pro | Built by Tidjani for CS50P. All rights reserved.", "", sep="\n")
    elif option == 2:
        print("", "Thank you for using Meal Prep Pro !", "", "2024 © Meal Prep Pro | \
Built by Tidjani for CS50P. All rights reserved.", "", sep="\n")

def here_is(option):
    if option == 'groceries list' or option == 'calorie intake':
        print("", f"↓↓↓ Here is your {option} for this menu ↓↓↓", "", sep="\n")
    elif option == 'menu':
        print("", "↓↓↓ Here is a menu generated by Meal Prep Pro ↓↓↓", "", sep="\n")

def display_table(option):
    print(tabulate(option, tablefmt="double_grid"), "", "© Meal Prep Pro", "", sep="\n")

def menu_generator(breakfasts, lunches, dinners):
    generated_menu = []
    generated_menu.append(days)
    generated_menu.append(breakfasts)
    breakfasts_temp = breakfasts.copy()
    breakfasts_temp.remove("BREAKFAST")

    generated_menu.append(lunches)
    lunches_temp = lunches.copy()
    lunches_temp.remove("LUNCH")

    generated_menu.append(dinners)
    dinners_temp = dinners.copy()
    dinners_temp.remove("DINNER")
    return generated_menu

def calorie_intake_table_maker(breakfasts, lunches, dinners):
    calorie_intake_menu = []
    calorie_intake_menu.append(days)

    breakfasts_temp = breakfasts.copy()
    breakfasts_temp.remove("BREAKFAST")
    breakfasts_temp = list(map(calorie, breakfasts_temp))
    breakfasts_temp.insert(0, "BREAKFAST")
    calorie_intake_menu.append(breakfasts_temp)

    lunches_temp = lunches.copy()
    lunches_temp.remove("LUNCH")
    lunches_temp = list(map(calorie, lunches_temp))
    lunches_temp.insert(0, "LUNCH")
    calorie_intake_menu.append(lunches_temp)

    dinners_temp = dinners.copy()
    dinners_temp.remove("DINNER")
    dinners_temp = list(map(calorie, dinners_temp))
    dinners_temp.insert(0, "DINNER")
    calorie_intake_menu.append(dinners_temp)

    total = ["TOTAL (cal.)"]
    for i in range(1, 8):
        total.append(int(breakfasts_temp[i]) + int(lunches_temp[i]) + int(dinners_temp[i]))

    calorie_intake_menu.append(total)
    return calorie_intake_menu


def groceries_list_maker(breakfasts, lunches, dinners):
    groceries_temp = []
    for i in breakfasts:
        if i != "BREAKFAST":
            groceries_temp.append(groceries_function(i))
    for j in lunches:
        if j != "LUNCH":
            groceries_temp.append(groceries_function(j))
    for k in dinners:
        if k != "DINNER":
            groceries_temp.append(groceries_function(k))
    groceries_temp = flatten(groceries_temp)

    final_list_groceries = []
    for item in set(groceries_temp):
        final_list_groceries.append(item)
    return final_list_groceries

def add_new_meal():
    new_meal = input("\nWhat meal do you want to add on the recipes list ? ").title()
    print("\nIs it a breakfast, lunch or dinner meal ? ")
    while True:
        try:
            new_meal_category = int(input("\n→ Tap 1 for breakfast\n→ Tap 2 for lunch\n→ Tap 3 for dinner\n\n$ "))
            allowed_categories = [1, 2, 3]
            if new_meal_category in allowed_categories:
                break
            print("Please enter 1, 2 or 3")
        except ValueError:
            print("Please enter 1, 2 or 3", '\n')

    if new_meal_category == 1:
        new_meal_writer(new_meal, 1)
    elif new_meal_category == 2:
        new_meal_writer(new_meal, 2)
    elif new_meal_category == 3:
        new_meal_writer(new_meal, 3)

    while True:
        try:
            new_calorie = int(input("\nPlease give us the calorie intake of your recipe\n$ "))
            with open("calories.csv", "a") as file:
                file.write(f'"{new_meal}";{new_calorie}\n')
            break
        except ValueError:
            print("Please enter a valid calorie intake.")

    print("", "Now please give us the different ingredients of your recipe.", "", 'How: → Write your items one by \
one, hit "Enter" every time you write one item.', "     → When you're done, please press control-D", "", sep="\n")
    ingredients_list = '"'
    while True:
        try:
            ingredients_list = ingredients_list + input("→ ") + ";"
        except EOFError:
            ingredients_list = ingredients_list[0:-1] + ingredients_list[-1].replace(";", "")
            ingredients_list += '"'
            print("\nYour recipe has been successfully added to the collection ✓\n")
            break

    with open("groceries.csv", "a") as file:
        file.write(f"\n{new_meal},{ingredients_list}")

if __name__ == "__main__":
    main()

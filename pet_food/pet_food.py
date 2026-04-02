import math

current_food_weight = 85
new_food_weight = 100
number_of_meals_a_day = 2
number_of_days = 14


def switch_food(current, new, meals, days):
    total_meals = meals * days
    current /= meals
    current_split = current / total_meals
    new /= meals
    new_split = new / total_meals

    print("Meal splits:")

    for meal in range(total_meals):
        current_meal = round(current - (meal * current_split))
        new_meal = round(meal * new_split)
        day = math.floor(meal / 2 + 1)
        meal_name = "Breakfast" if meal % 2 == 0 else "Dinner"
        print(
            f"Day {str(day) + ' ' if day < 10 else day} | {meal_name + '   ' if len(meal_name) < 8 else meal_name} | Current food: {current_meal}, New food: {new_meal}")

    # on meal 1 I want to have 100% of current food
    # on last meal, I want to have 0% of current food, 100% of new food
    # I want to incrementally decrease current food and increase new food
    # print("current split", current_split, "new split", new_split)


switch_food(current_food_weight, new_food_weight,
            number_of_meals_a_day, number_of_days)

# print("Welcome to Pet Food Switcher\n")

# print("Please enter your current food weight in digits:")
# current_food_weight = int(input())

# print("\nPlease enter your new food weight in digits:")
# new_food_weight = int(input())

# print("\nPlease enter the number of meals per day:")
# number_of_meals_a_day = int(input())

# print("\nPlease enter of the number of days to transition from the current food to new food:")
# number_of_days = int(input())

# print(f"\nYou have selected:\n\
#     current food weight: {current_food_weight}\n\
#     new food weight: {new_food_weight}\n\
#     number of meals a day: {number_of_meals_a_day}\n\
#     number of days: {number_of_days}")

# switch_food(current_food_weight, new_food_weight,
#             number_of_meals_a_day, number_of_days)

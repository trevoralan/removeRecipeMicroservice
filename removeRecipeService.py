# Remove Recipe Microservice
# Trevor Gililland
# CS 361 - Winter 2025

import time

displayActLoc = './ActionFolder/displayActions.txt'
shopListActLoc = './ActionFolder/shoppingListActions.txt'

recipe = ''

def recipe_check(action_path, meal_path):
    """Monitors an action file for a meal to remove and if a meal is found, it will try to remove it from the plan"""

    while True:
        time.sleep(1)  # Check for changes every 1 second

        with open(action_path, 'r+') as f:
            read_data = f.read()  # Read in action file
            f.seek(0)
            f.truncate()

        try:
            # Get Recipe Name and create File
            if read_data == "start":
                dispFile = open(displayActLoc, 'w')
                dispFile.write(
                    "shop:remo:star" + "Which Recipe do you wish to remove?\n Type name as it displays in the shopping cart then hit enter: ")
                dispFile.close()
            elif read_data != "start" and read_data != "yes" and read_data != "no" and read_data != "":
                # ask user if they're sure they want to remove
                recipe = read_data
                dispFile = open(displayActLoc, 'w')
                dispFile.write(
                    "shop:remo:conf" + "Are you sure you wish to remove " + read_data + "?\n Type (yes/no): ")
                dispFile.close()
            elif read_data == "yes":
                # if confirm, check if recipe exists
                i = 0  # Set test for updates
                meal_array = []  # Set empty meal plan array
                """Read in meal plan and assign to the meal plan array then close file"""
                meal_plan = open(meal_path, 'r')
                for meal in meal_plan:
                    meal = meal.removesuffix("\n")
                    meal_array.append(meal)
                meal_plan.close()
                """Test the read in recipe against the meal plan array and remove if found"""
                for item in meal_array:
                    if item == recipe:
                        meal_array.remove(recipe)
                        i = 1
                """If recipe was removed, write done to action file and write back new plan"""
                if i == 1:
                    dispFile = open(displayActLoc, 'w')
                    dispFile.write("shop:remo:done" + "The recipe " + recipe + " was successfully removed.")
                    dispFile.close()
                    with open(meal_path, 'w') as m:
                        for item in meal_array:
                            m.write(item + "\n")
                elif i == 0:  # If no recipe was removed, write none to action file
                    dispFile = open(displayActLoc, 'w')
                    dispFile.write("shop:remo:none" + "The recipe " + recipe + " is already not in the shopping cart.")
                    dispFile.close()
            elif read_data == "no":
                shopFile = open(shopListActLoc, 'w')
                shopFile.write("start")
                shopFile.close()

        except ValueError:
            """Do nothing on error and try again"""


if __name__ == '__main__':
    recipe_check('./ActionFolder/removeMealActions.txt', './ActionFolder/mealPlan.txt')

# What is this microservice?
This remove recipe microservice is meant to assist a user in removing a recipe from their shopping cart. It works along other microservices to guide the user through building a healthy lifestyle, helping them build recipes and then proceed to go shopping for the ingredients to make them.

# How to use the microservice
This microservice is dependent on its own txt file (removeMealActions.txt) that it receives commands from to action upon. The first command it expects to receive is the "start" command, which triggers it to communicate messages to the display service's txt file to interact with the user. An example of this:
```
removeRecipeFile = open('./ActionFolder/removeMealActions.txt', 'w')
removeRecipeFile.write("start")
removeRecipeFile.close()
```
The message it will send back starts with "shop:remo:star", followed by a message asking the user which receipe they would like to remove. An example of this response is:
```
dispFile = open('./ActionFolder/displayActions.txt', 'w')
dispFile.write(
    "shop:remo:star" + "Which Recipe do you wish to remove?\n Type name as it displays in the shopping cart then hit enter: ")
dispFile.close()
```
The second command it expects to receive is a recipe from the user that they want to remove from the existing mealPlan.txt file. An example of this:
```
userInput = input()
removeFile = open('./ActionFolder/removeMealActions.txt', 'w')
removeFile.write(userInput)
removeFile.close()
```
It will log the recipe, then reach out to the display service's txt file to ask the user if indeed they want to remove this recipe. The message it will send back starts with "shop:remo:conf", followed by a message asking the user if they are sure they would like to remove this recipe. An example of this is:
```
dispFile = open('./ActionFolder/displayActions.txt', 'w')
dispFile.write(
    "shop:remo:conf" + "Are you sure you wish to remove " + read_data + "?\n Type (yes/no): ")
dispFile.close()
```
The third command it expects to receive is either a yes or no from the user, which will determine if the recipe is removed or not. If the no command is received, it will write "Start" to the shopping list service's action txt file, which will take the user back to the main menu. An example of this is:
```
shopFile = open('./ActionFolder/shoppingListActions.txt', 'w')
shopFile.write("start")
shopFile.close()
```
If the yes command is received, it will then check the mealplan.txt file for the recipe and if it doesn't exist, it will communicate to the display service's txt file that the recipe does not exist. The message it will send back starts with "shop:remo:none", followed by a message letting the user know the recipe is not in the shopping cart. If the recipe does exist in the mealPlan.txt file, it will communicate to the display service's txt file that the recipe has been removed, remove the recipe from the shopping cart and write the new cart back to mealPlan.txt. The message it will send back starts with "shop:remo:done", followed by a message letting the user know the recipe has been removed from the shopping cart. An example of this is:
```
dispFile = open('./ActionFolder/displayActions.txt', 'w')
dispFile.write("shop:remo:done" + "The recipe " + recipe + " was successfully removed.")
dispFile.close()
```
The service has a subfolder, ActionFolder, where the removeMealActions.txt, displayActions.txt, shoppingListActions.txt, and mealPlan.txt files are located and expected to be able to be read/written from in order to action upon.

# UML Sequence Diagram


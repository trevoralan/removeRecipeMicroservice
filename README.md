# What is this microservice?
This remove recipe microservice is meant to assist a user in removing a recipe from their shopping cart. It works along other microservices to guide the user through building a healthy lifestyle, helping them build recipes and then proceed to go shopping for the ingredients to make them.

# How to use the microservice
This microservice is dependent on its own txt file (removeMealActions.txt) that it receives commands from to action upon. The first command it expects to receive is the "start" command, which triggers it to communicate messages to the display service's txt file to interact with the user. The message it will send back starts with "shop:remo:star", followed by a message asking the user which receipe they would like to remove. 

The second command it expects to receive is a recipe from the user that they want to remove from the existing mealPlan.txt file. It will log the recipe, then reach out to the display service's txt file to ask the user if indeed they want to remove this recipe. The message it will send back starts with "shop:remo:conf", followed by a message asking the user if they are sure they would like to remove this recipe. 

The third command it expects to receive is either a yes or no from the user, which will determine if the recipe is removed or not. If the no command is received, it will write "Start" to the shopping list service's action txt file, which will take the user back to the main menu. If the yes command is received, it will then check the mealplan.txt file for the recipe and if it doesn't exist, it will communicate to the display service's txt file that the recipe does not exist. The message it will send back starts with "shop:remo:none", followed by a message letting the user know the recipe is not in the shopping cart. If the recipe does exist in the mealPlan.txt file, it will communicate to the display service's txt file that the recipe has been removed, remove the recipe from the shopping cart and write the new cart back to mealPlan.txt. The message it will send back starts with "shop:remo:done", followed by a message letting the user know the recipe has been removed from the shopping cart.

The service has a subfolder, ActionFolder, where the removeMealActions.txt, displayActions.txt, shoppingListActions.txt, and mealPlan.txt files are located and expected to be able to be read/written from in order to action upon.

# UML Sequence Diagram
![UML Sequence Diagram](https://github.com/trevoralan/removeRecipeMicroservice/blob/main/UML.png)

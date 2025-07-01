# storage of todos
todos = [] 

# while loop for managing todos
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() # in case the user accidentally enters a space before or after the input
    user_action = user_action.lower() # in case the user enters an uppercase letter

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            
            # open the txt file to save its contents
            file = open("todos.txt", "r")
            todos = file.readlines() #stores contents in a list
            todos.append(todo)
            file.close()

            # overwrite txt file with the added todo
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todos.txt", "r")  # open todos.txt in read mode
            todos = todos.readlines() # .readlines() will return a list
            file.close()

            # loop through the list and print the concatenated index-item name
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        case "edit":
            number = int(input("Number of the todo you want to edit: "))
            number = number - 1
            new_todo = input("What would you like to change it to? ")
            todos[number] = new_todo
        case "complete":
            number = int(input("Number of the todo you want to complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        case _:
            print("Unknown command")
print("Bye!")

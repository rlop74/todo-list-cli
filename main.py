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
            with open("todos.txt", "r") as file:
                todos = file.readlines() # returns list value, store in todos
            
            # add new todo
            todos.append(todo)

            # overwrite txt file with the added todo
            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":
            # open txt file and save contents in todos (returns list)
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            # accomplish the same thing for removing extra \n, but using list comprehension
            # new_todos = [item.strip("\n") for item in todos]

            # loop through the list and print the concatenated index-item name
            for index, item in enumerate(todos):
                item = item.strip("\n") # remove extra \n
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

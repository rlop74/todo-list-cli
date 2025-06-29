# storage of todos
todos = [] 

# while loop for managing todos
while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    user_action = user_action.lower()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index}-{item}")
        case "edit":
            number = int(input("Number of the todo you want to edit: "))
            number = number - 1
            new_todo = input("What would you like to change it to? ")
            todos[number] = new_todo
        case "exit":
            break
        case _:
            print("Unknown command")
print("Bye!")

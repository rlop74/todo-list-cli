# storage of todos
todos = [] 

# while loop for managing todos
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip() # in case the user accidentally enters a space before or after the input
    user_action = user_action.lower() # in case the user enters an uppercase letter

    if "add" in user_action:
        todo = user_action[4:]
        
        # open the txt file to save its contents
        with open("todos.txt", "r") as file:
            todos = file.readlines() # returns list value, store in todos
        
        # add new todo
        todos.append(todo)

        # overwrite txt file with the added todo
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        # open txt file and save contents in todos (returns list)
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        # remove extra \n using list comprehension
        # new_todos = [item.strip("\n") for item in todos]

        # loop through the list and print the concatenated index-item name
        for index, item in enumerate(todos):
            item = item.strip("\n") # remove extra \n
            print(f"{index + 1}-{item}")

    elif "edit" in user_action:
        # get user input
        number = int(user_action[5:])
        number = number - 1
        new_todo = input("What would you like to change it to? ")

        # open file in read mode
        with open("todos.txt", "r") as file:
            todos = file.readlines()
        
        todos[number] = new_todo + "\n"
        
        # open file in write mode and edit todo
        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])
        
        with open("todos.txt", "r") as f:
            todos = f.readlines()

        removed_todo = todos.pop(number - 1)
        
        with open("todos.txt", "w") as f:
            f.writelines(todos)

        message = f"{removed_todo.strip("\n")} was removed from the list."
        print(message)

    elif "exit" in user_action:
        break

    else:
        print("Command is not valid.")

print("Bye!")

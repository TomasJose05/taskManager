from task_manager import TaskManager

def print_menu():
        print("---- Task Manager ----") 
        print("1. Add task") 
        print("2. List tasks")  
        print("3. Complete task")  
        print("4. Delete task") 
        print("5. Quit")        



def main():
    manager = TaskManager()

    while True:

        print_menu()

        choice = input("Choose an Option: ")

        match choice:
            case "1":
                description = input("Task description: ")
                manager.add_task(description)

                
            case "2":
                manager.list_tasks()


            case "3":
                id = input("ID of the task to complete: ")
                manager.complet_task(id)


            case "4":
                id = input("ID of the task to delete: ")
                manager.delete_task(id)


            case "5":
                print("Quiting ...")
                break
            case _:
                print("Is not a valid option, select a valid option please.")

if __name__ == "__main__":
    main()                 
from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
        print("---- Task Manager ----") 
        print("1. Add task") 
        print("2. Add complex task (With AI)")
        print("3. List tasks")  
        print("4. Complete task")  
        print("5. Delete task") 
        print("6. Quit")        



def main():
    manager = TaskManager()

    while True:

        print_menu()

        try:

            choice = int(input("Choose an Option: "))

            match choice:
                case 1:
                    description = input("Task description: ")
                    manager.add_task(description)

                case 2:
                    description = input("Complex Task description: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error:"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break    

                    
                case 3:
                    manager.list_tasks()


                case 4:
                    id = int(input("ID of the task to complete: "))
                    manager.complet_task(id)


                case 5:
                    id = int(input("ID of the task to delete: "))
                    manager.delete_task(id)


                case 6:
                    print("Quiting ...")
                    break
                case _:
                    print("Is not a valid option, select a valid option please.")
        except ValueError:
            print("Is not a valid option, select a valid option please.")            
if __name__ == "__main__":
    main()                 
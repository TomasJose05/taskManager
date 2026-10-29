class Task:
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed

    def __str__(self):
        status =  "✓" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"


class TaskManager:
    def __init__(self):
        self._tasks =  []
        self._next_id = 1

    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {description}")

    def list_tasks(self):
        if not self._tasks:
            print("There are no tasks to show")
        else:
            for task in self._tasks:
                print(task)

    def complet_task(self, id):
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Task Complete: {task}")
                return
        print(f"No tasked found with this #{id}")

    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task deleted: #{id}")
                return
        print(f"Task don't found: #{id}")

        
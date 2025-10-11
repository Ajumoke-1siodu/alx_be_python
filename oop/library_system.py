import os
import json

class TodoList:
    def __init__(self, filename="todo_data.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
    
    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save_tasks()
    
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
    
    def list_tasks(self):
        for i, t in enumerate(self.tasks):
            status = "✓" if t["done"] else "✗"
            print(f"{i + 1}. [{status}] {t['task']}")

def main():
    todo = TodoList()
    while True:
        print("\nTo-Do List:")
        todo.list_tasks()
        print("\nOptions:")
        print("1 - Add Task")
        print("2 - Mark Task as Done")
        print("3 - Delete Task")
        print("4 - Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter new task: ")
            todo.add_task(task)
        elif choice == "2":
            idx = int(input("Enter task number to mark as done: ")) - 1
            todo.mark_done(idx)
        elif choice == "3":
            idx = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(idx)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

"""Simple To-Do list console application where users can add, view, and delete tasks. tasks are added to seperate file"""

import datetime


class Task:
    tasks = []
    def __init__(self, name, date_created):
        self.name  = name
        self.date_created = date_created

    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task_num):
        if task_num <=  len(self.tasks) and task_num > 0:
            del self.tasks[task_num-1]
        else:
            print("Task does not exist")
    def display_all_tasks(self):
        print(f"-------{self.name}-------\nCreated: {self.date_created}\n")
        for i in range(len(self.tasks)):
            print(f"{i+1}. {self.tasks[i]}")
        print("\n")

    def save(self):
        with open(f"{self.name.replace(' ', '_')}.txt", "a") as file:
            file.write(f"-------{self.name}-------\nCreated: {self.date_created}\n")
            for i in range(len(self.tasks)):
                file.write(f"{i+1}. {self.tasks[i]}\n")
        print("to-do list succesfully saved.")
        pass

def main():
    print("-------To-Do-list-application-------")
    print("1. Create New To-do list\n2. Add Task\n3. Remove Task\n4. Save To-do list\n5. Quit")
    try:
        choice=int(input("Enter option: "))
    except:
        print("invalid option")
        return
    task_list = None
    while choice != 5:
        if choice == 1:
            if(task_list is not None):
                response = input("You have an unsaved to-do list, would you like to save it before creating a new one? Y/N: ").lower()
                if response == "y":
                    task_list.save()
            name = input("Name of new to-do list: ")
            task_list = Task(name, str(datetime.datetime.now()))
        if choice == 2:
            task_list.add_task(input("Add a new task: "))
            task_list.display_all_tasks()
        if choice == 3:
            task_list.remove_task(int(input("Enter the task number you wish to delete: ")))
            task_list.display_all_tasks()
        if choice == 4:
            task_list.save()

        try:
            choice=int(input("Enter option: "))
        except:
            print("invalid option")


if __name__ == "__main__":
    main()
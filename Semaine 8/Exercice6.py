Tasks = []
def add_tasks():
    number_of_tasks = int(input("Enter the number of new tasks: "))
    for i in range(number_of_tasks):
        task = input("\nEnter the name of the task: ")
        category = input("Enter the category of the task: ")
        duration = input("Enter the duration of the task: ")
        priority = input("Enter the priority of the task (out of 10): ")
        task_dict = dict(task=task, category=category, duration=duration, priority=priority)
        Tasks.append(task_dict)

add_tasks()

def delete_task():
    task = input("Enter the name of the task to delete: ")
    for i in range(len(Tasks)):
        if Tasks[i]['task'] == task:
            del Tasks[i]
            print("Task deleted")
            break
        else:
            print("Task not found, make sure you typed the name correctly")

       
def display_tasks_for_cat():
    Tasks.sort(key=lambda x: x['priority'])
    category = input("Enter the category of the tasks to display: ")
    for i in range(len(Tasks)):
        if Tasks[i]['category'] == category:
            print(Tasks[i]['task'])

# display_tasks_for_cat()

def display_total_duration_per_cat():
    category = input("Enter the category of the tasks to display: ")
    total_duration_per_cat = 0
    for i in range(len(Tasks)):
        if Tasks[i]['category'] == category:
            total_duration_per_cat += int(Tasks[i]['duration'])
    print(f"The total duration of the tasks in the category {category} is: {total_duration_per_cat} ")
    
    total_duration = 0
    for i in range(len(Tasks)):
        total_duration += int(Tasks[i]['duration'])
    print(f"The total duration of the tasks is: {total_duration} ")
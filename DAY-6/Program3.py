#Build a to_do list app that saves tasks to a .txt file
def add_task(task) :
    with open("todo.txt" , "a") as f :
        f.write(task + "\n")
        print(f"Added : '{task}'")
def view_tasks() :
    print("\n---To-Do List ---")
    try :
         with open("todo.txt" , "r") as f :
             tasks = f.readlines()
             if not tasks :
                 print("No tasks found!")
             else :
                 for i , task in enumerate(tasks , 1):
                     print(f"{i}. {task.strip()}")
    except FileNotFoundError :
         print("No to-do list found!")
print("----------------")
#running the app
add_task("Complete your assignment ")
add_task("Study python ")
view_tasks()
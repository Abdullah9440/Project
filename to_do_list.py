task = []

def add_task ():
    add_work =input('task name : ')
    task.append(add_work)
    
def view_task():
    if len(task) == 0:
        print('the task is empty')
    else:
        for i in range(len(task)):
            print(str(i+1) +'.' + task[i])
def delete_task():
    for i in range(len(task)):
        print(str(i+1) +'.' + task[i])
                
    delete_task = int(input('whice task you wanna delete?'))
    del task[delete_task - 1]
            

while True:
    # show menu every time
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_task()
     
    elif choice == 2:
        view_task()
        
    elif choice == 3:
        delete_task()
        
    elif choice == 4:
        print('goodbye')
        break
        
    else:
        print('invalid input')
        
        
        
        
        
  


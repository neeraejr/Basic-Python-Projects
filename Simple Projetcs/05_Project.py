# Project --> TO-DO List Manager
Tasks = []
def AddTask():
    # Tasks = []
    Task = int(input("Enter No. of Tasks Added: "))
    for i in range(Task):
        Tsk = input("Enter Task: ")
        Tasks.append(Tsk)
    else:
        for index,task in enumerate(Tasks, start=1):
            print(f"Task {index} - {task}")

def ViewTask():
    print("\n\tTasks\n")
    for index,task in enumerate(Tasks, start=1):
            print(f"Task {index} - {task}")
    else:
        print("Sorry, There is no Tasks.\n")

def MarkComplete():
    pass    

def DeleteTask():
    pass

def main():
    while True:
        print("Choose an operation:  \n1 --> Add Task\n2 --> View Task\n3 --> Mark Complete\n4 --> Delete Task\n5 --> Exit")
        operaion = input("Choose Operation:")
        if operaion == "1":
            AddTask()
        elif operaion == "2":
            ViewTask()
        elif operaion == "3":
            MarkComplete()
        elif operaion == "4":
            DeleteTask()
        elif operaion == "5":
            break
        else:
            print("Invalid Input, Please try again.")
        
main()
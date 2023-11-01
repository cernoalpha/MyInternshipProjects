
class Task:
  def __init__(self,id, title, dueDate, desc, completed= False):
    self.id= id
    self.title = title
    self.dueDate = dueDate
    self.desc = desc
    self.completed = completed

class toDoList:
  def __init__(self):
    self.tasks=[]

  def addTask(self, task):
    self.tasks.append(task)

  def removeTask(self, id):
    for task in self.tasks:
      if task.id == id:
        self.tasks.remove(task)
        print("Task deleted")
        return
    else:
        print("ID not found in the list.")

  def updateTask(self,id,new_title= None,new_dueDate= None,new_desc= None):
    for task in self.tasks:
      if task.id == id:
         if new_title is not None:
            task.title = new_title
         if new_dueDate is not None:
            task.dueDate = new_dueDate
         if new_desc is not None:
            task.desc = new_desc
         print("Task updated")
         return
      else:
        print("ID not found in the list.")

  def completeTask(self, id):
    for task in self.tasks:
      if task.id == id:
        task.completed = True
        print("Task set as Completed")
        return
    else:
        print("ID not found in the list.")


  def getTaskDetails(self, task_id= None):
     if task_id is None:
        return self.tasks
     for task in self.tasks:
        if task.id == task_id:
            return task

ID = 0
def genID():
    global ID
    ID += 1
    return ID

todo_list = toDoList()

while True:
    print()
    print("1. Display To-do List")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Complete Task")
    print("6. Exit")

    opt = int(input("Enter Option: "))

    if opt == 1:
        all_tasks = todo_list.getTaskDetails()
        completed_tasks = []
        incomplete_tasks = []

        for task in all_tasks:
            if task.completed:
                completed_tasks.append(task)
            else:
                incomplete_tasks.append(task)


        if len(completed_tasks) == 0:
          print()
          print("-------------------------------------------------------------")
          print("No Completed Tasks")
          print("-------------------------------------------------------------")
        else:
          print()
          print("-------------------------------------------------------------")
          print("Completed Tasks:")
          print()
          for task in completed_tasks:
            print(f"Task ID: {task.id} Title: {task.title} Due Date: {task.dueDate} Description: {task.desc}")
          print("-------------------------------------------------------------")

        if len(incomplete_tasks) == 0:
           print()
           print("*************************************************************")
           print("No Incomplete Tasks")
           print("*************************************************************")
        else :
         print()
         print("*************************************************************")
         print("Incomplete Tasks:")
         print()
         for task in incomplete_tasks:
            print(f"Task ID: {task.id} Title: {task.title} Due Date: {task.dueDate} Description: {task.desc}")
         print("*************************************************************")

    elif opt == 2:
        title = input("Title: ")
        dueDate = input("Due Date: ")
        desc = input("Description: ")
        task = Task(genID(), title, dueDate, desc)
        todo_list.addTask(task)

    elif opt == 3:
        task_id = int(input("ID: "))
        todo_list.removeTask(task_id)

    elif opt == 4:
        task_id = int(input("ID: "))
        title = input("New Title (Enter to skip): ")
        dueDate = input("New Due Date (Enter to skip): ")
        desc = input("New Description (Enter to skip) : ")
        if not title:
          title = None
        if not dueDate:
          dueDate = None
        if not desc:
          desc = None
        todo_list.updateTask(task_id, title, dueDate, desc)

    elif opt == 5:
        task_id = int(input("ID: "))
        todo_list.completeTask(task_id)

    elif opt == 6:
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid option. Please select a valid option (1-6).")
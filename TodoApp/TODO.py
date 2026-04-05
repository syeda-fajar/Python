
import json
import os 
class Todo:
    def __init__(self,file_path):
        self.file_path = file_path
        if os.path.exists(file_path):
           with open(self.file_path,'r', encoding='utf-8') as file:
               self.todos = json.load(file)
        else:
            self.todos=[]
    
    def addTodo(self,task):
        Todo={"Task":task,"Done":False}
        self.todos.append(Todo)
        self.save()
        
    def deleteTodo(self,position):
        try:
                del self.todos[position-1]
                self.save() 
        except IndexError:
            print ("Invalide postion : position dont exisit")
    def save(self):
         with open(self.file_path,'w', encoding='utf-8') as file:
             json.dump(self.todos,file)
    def showTodo(self):
        for i, todo in enumerate((self.todos),start=1):
            if todo["Done"]:
                status="Done"
            else:
                status="Not Done"
            print(f"{i}:{todo['Task']}-{status}")
            
obj1 = Todo('todo.json')
while(True):
    print("welcome to your daily Todo")
    print("press 1 for showing Todo")
    print("press 2 for adding task")
    print("press 3 for Delete task")
    print("press 0 for exit")
    try:
        choice = int(input("please enter you choice"))
        if(choice==1):
          obj1.showTodo()
        elif(choice==2):
         task = input("enter the task ")
         obj1.addTodo(task)
        elif(choice==3):
          pos = int(input("enter the postion of task to delete  "))
          obj1.deleteTodo(pos)
        elif(choice==0):
          exit()
    except ValueError:
        print("Please enter a valid number")

    
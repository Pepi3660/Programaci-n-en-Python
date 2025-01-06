todo_list = []

while True:
  
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1
  
  print("Options: ")
  print("1) Add Task")
  print("2) Remove Task")
  print("3) Quit")
  choice = input()
  
  if choice == "1":
    new_task = input("Enter the task: ")
    todo_list.append(new_task)
    print("Adding task")
    print(f"Task {new_task} added")
  elif choice == "2":
    if not todo_list:
      print("Your ToDo list is empty")
    else:
      remove_task = todo_list.pop()
      print("Removing task")
      print(f"remove task: {remove_task}")
  elif choice == "3":
    print("Quitting")
    break

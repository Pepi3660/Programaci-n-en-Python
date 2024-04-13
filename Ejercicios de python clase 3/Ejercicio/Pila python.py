import os

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print("Pushed:", item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack Empty")

    def show_stack(self):
        if not self.is_empty():
            print("Stack contents:")
            for index, item in enumerate(reversed(self.items), start=1):
                print(f"|{item}| [{len(self.items) - index + 1}] {'-> top stack' if index == 1 else ''}")
        else:
            print("Stack is empty")

# Función para limpiar la pantalla
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


#CUERPO DEL PROGRAMA
stack = Stack()
while True:
    clear_screen()
    print("\t\tMenu:\n")
    print("\t\t1. Push")
    print("\t\t2. Pop")
    print("\t\t3. Show Stack")
    print("\t\t4. Exit")
    choice = input("\n\t\tEnter your choice: ")
    
    if choice == '1':
        clear_screen()
        item = input("Enter item to push: ")
        stack.push(item)
        input("Press Enter to continue...")
    elif choice == '2':
        clear_screen()
        popped_item = stack.pop()
        if popped_item is not None:
            print("Popped:", popped_item)
        input("Press Enter to continue...")
    elif choice == '3':
        clear_screen()
        stack.show_stack()
        input("Press Enter to continue...")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        input("Press Enter to continue...")

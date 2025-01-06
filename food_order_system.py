italian_food = [
  "Pasta Bolognese", 
  "Pepperoni pizza",
  "Margherita pizza", 
  "Lasagna"
]

indian_food = [
    "Curry", 
    "Chutney", 
    "Samosa", 
    "Naan"
]

def find_meal(name, menu):
 return name if name in menu else None

def select_meal(name, cuisine):
  if(cuisine == "Italian"):
    return find_meal(name, italian_food)
  elif(cuisine == "Indian"):
    return find_meal(name, indian_food)
  else:
    return None

def display_available_meals(food_type):
  if(food_type == "Italian"):
    print("Available Italian Meals")
    for food in italian_food:
      print(food)
  elif food_type == "Indian":
    print("Available Indian Meals")
    for food in indian_food:
      print(food)
  else:
    print("Invalid food type")

  
def create_summary(name, amount, cuisine):
  order = select_meal(name, cuisine)
  if order:
    return f"You ordered {amount} {order}"
  else:
    return "Meal not found"
  
print("Welcome to the Food Order System!")
type_input = input("Enter the type of food you want to order: ")
display_available_meals(type_input)
name_input = input("Enter the meal name: ")
amount_input = int(input("Enter the quantity: "))

result = create_summary(name_input, amount_input, type_input)
print(result)
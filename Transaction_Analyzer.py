import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")

#print_transactions(data)

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(total_deposited)
  withdrawal = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawls = sum(withdrawal)
  print(total_withdrawls)
  balance = total_deposited + total_withdrawls
  print(f"Balance: {balance}")

#print_summary(data)

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"Largest witdrawals: {largest_withdrawal}")
  print(f"Largest deposit: {largest_deposit}")

  deposits = [transaction[0] for transaction in transactions
  if transaction[0] >= 0]
  total_deposit = sum(deposits)
  average_deposit = total_deposit / len(deposits) if deposits else 0
  print(f"Average deposit: {average_deposit}")

  withdrawals = [transaction[0] for transaction in transactions 
  if transaction[0] < 0]
  total_withdrawals = sum(withdrawals)
  average_withdrawal = total_withdrawals / len(withdrawals) if withdrawals else 0
  print(f"Average withdrawal: {average_withdrawal}")

while True:
  print("  *-----M E N U-----*")
  print("   1. Print")
  print("   2. Analyze")
  print("   3. Stop")
  choice = int(input("    Choice: "))
  print("")
    
  match choice:
    case 1: print_summary(data)
    case 2: analyze_transactions(data)
    case 3: break
    case default: print("Invalid option!")
  
  input("Press any key to continue.....")
  clear_screen()
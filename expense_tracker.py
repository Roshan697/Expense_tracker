import os
expense = []

def load_from_file():
    if os.path.exists("expenses.txt"):
        with open("expenses.txt","r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    expense.append({"name": parts[0], "amount": float(parts[1])})
        print("previous expenses loaded!!")   
load_from_file()         

def add_expense(name, amount):
    
    try: 
        amount = float(amount)
        expense.append({"name":name, "amount":amount})
        print(f"Added: {name} -${amount}")
    except ValueError:
        print("Invalid amount! please a number")
        
        
        
    
def view_expenses():
    total = 0
    for e in expense:
        
        
        print(f"{e['name']} - ${e['amount']}")
        total += e['amount']
    print(f"total : ${total}")

def save_to_file():
    with open("expenses.txt","w") as f:
        for e in expense:
            f.write(f"{e['name']},{e['amount']}\n")
    print("Saved!!")
    
def delete_expense():
    if len(expense) == 0:
        print("No expenses to delete")
        return
    view_expenses()
    

    name = (input("Enter the expense name to delete: ").strip().lower())
        
    for e in expense:
        if e['name'].lower() == name:
                expense.remove(e)
                print(f"Deleted: {e['name']} --> ${e['amount']}")
                return
    print(f"expense {name} not found! ")
        
    
while True:
    print("\n 1. add \n 2. view\n 3. save \n 4.to delete any expense\n 5. exit")
    choice = input("Choice : ")
    
    if choice == "1":
        add_expense(input("Name: "), (input("Amount: "))) 
    
    elif choice == "2":
        view_expenses()
    
    elif choice == "3":
        save_to_file()
        
    elif choice == "4":
        delete_expense()
        
    elif choice == "5":
        break  
        
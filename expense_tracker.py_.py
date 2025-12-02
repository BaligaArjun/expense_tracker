import pandas as pd
import numpy as np 


Salary = float(input("Enter your total salary"))
expenses = []
while True:
    expense_name = input("\nEnter expense name (or type 'done' to finish): ")
    if expense_name.lower() == "done":
        break
    try:
        expense_amount = float(input(f"Enter your amount for {expense_name}: "))
    except ValueError:
        print(" please enter a vaild number for amount.")
        continue
    expenses.append({"Expense": expense_name, "Amount": expense_amount})
    print("Expense added! if you are finished, type 'done' next time for expense name.")
    df = pd.DataFrame(expenses)
    
    total_expense = np.sum(df["Amount"]) if not df.empty else 0
    remaining_balance = Salary - total_expense
    print("\n--- Expense Summary ---")
    if not df.empty:
        print(df.to_string(index=False))
    else:
        print("no expense entered.")
    print(f"\ntotal Expense: {total_expense}")
    print(f"Remaining Balance: {remaining_balance}")


    

import csv
import matplotlib.pyplot as plt

income_list = []
expense_list = []
save_list = []
tran_list = []

while True:

    print("""
=========================================
          EXPENSE TRACKER
=========================================
1.Add Income
2.Add Expense
3.Add Transaction
4.View Transactions
5.Show Expense Categories
6.Monthly Savings
7.Save Data to CSV
8.Expense Pie Chart
9.Monthly Saving Graph
10.Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":

        month = input("Month: ")
        amount = int(input("Income: "))

        income_list.append({
            "Month": month,
            "Amount": amount
        })

        print("Income added.")

    elif choice == "2":

        category = input("Category: ")
        spend = int(input("Amount: "))

        expense_list.append({
            "Category": category,
            "Spend": spend
        })

        print("Expense added.")

    elif choice == "3":

        to = input("To: ")
        sent = int(input("Amount: "))

        tran_list.append({
            "To": to,
            "Sent": sent
        })

        print("Transaction added.")

    elif choice == "4":

        print("\n=========================================")
        print("        TRANSACTION RECORD")
        print("=========================================")

        print(f"{'S.No':<6}{'Name':<20}{'Amount':>10}")
        print("-" * 40)

        count = 1
        total = 0

        for t in tran_list:
            print(f"{count:<6}{t['To']:<20}{t['Sent']:>10}")
            total += t["Sent"]
            count += 1

        print("-" * 40)
        print(f"{'Total':<26}{total:>10}")

    elif choice == "5":

         print("\n=========================================")
         print("        EXPENSE RECORDS")
         print("=========================================")

         print(f"{'S.No':<6}{'Category':<20}{'Amount':>10}")
         print("-" * 40)
    
         total = 0
         count = 1
    
         for e in expense_list:
             print(f"{count:<6}{e['Category']:<20}{e['Spend']:>10}")
             total += e["Spend"]
             count += 1
    
             print("-" * 40)
             print(f"{'Total Expense':<26}{total:>10}")

    elif choice == "6":
         month = input("Month: ")
         income = int(input("Monthly Income: "))
         expense = int(input("Total Expense: "))

         saving = income - expense

         save_list.append({
            "Month": month,
            "Saving": saving
         })

         print("Monthly Saving:", saving)

       
    elif choice == "7":

        with open("expense.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["Category", "Amount"])

            for e in expense_list:
                writer.writerow([e["Category"], e["Spend"]])

        print("CSV saved successfully.")

    elif choice == "8":

        categories = []
        amounts = []

        for e in expense_list:
            categories.append(e["Category"])
            amounts.append(e["Spend"])

        if len(categories) == 0:
            print("No data available.")

        else:
            plt.pie(amounts, labels=categories, autopct="%1.1f%%")
            plt.title("Expense Categories")
            plt.show()
            
    elif choice == "9":

        months = []
        savings = []

        for s in save_list:
            months.append(s["Month"])
            savings.append(s["Saving"])

        if len(months) == 0:
            print("No saving data.")

        else:
            plt.plot(months, savings, marker="o")
            plt.xlabel("Month")
            plt.ylabel("Saving")
            plt.title("Monthly Savings")
            plt.show()

    elif choice == "10":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
        
import pandas as pd
from pathlib import Path
import os
import csv
def loanTable(interest, p, r, t, loanDict, payment):
    num = 12 * int(t)
    for i in range(num):
        interest = (p * (r/12))
        principal = payment - interest
        p = p - principal
        loanDict["Loan Amount"].append(p)
        loanDict["Interest"].append(interest)
        loanDict["Principal"].append(principal)
print("Welcome to the Loan Generator")

loan = input("What is your loan amount?")
rate = input("What is your interest rate?")
time = input("What is the term of the loan?")

p = float(loan)
r = float(rate)
t = float(time)

payment = 0
interest = (p * (r/12))
payment = interest * ((1 + r/12)**(12*t))/((1 + r/12)**(12*t) - 1)
loanDict = {
    "Loan Amount": [],
    "Interest": [],
    "Principal": [], 
}
loanTable(interest, p, r, t, loanDict, payment)
while True:
    print("1. Monthly Payment Amount")
    print("2. Get Loan Amounts Generated")
    print("3. Increase Principal and Generate How Many Months Less of Payments")
    print("4. When Does My Principal Become Larger Than My Interest")
    print("5. How Much Will You Pay In Total On The Loan")
    print("6. Quit")
    userInput = input("Choose an option: ")
    if userInput == "1":
        print("Your monthly payment amount is $" + str(round(payment, 2)))
    elif userInput == "2":
        dataTable = pd.DataFrame(loanDict)
        # filepath = Path('C:/Users/travismaekawa/Desktop/PythonCode/loanTable.csv')  
        # filepath.parent.mkdir(parents=True, exist_ok=True)  
        # dataTable.to_csv(filepath)
        os.makedirs('Desktop/PythonCode', exist_ok=True)  
        dataTable.to_csv('Desktop/PythonCode/loanTable.csv')    
        # dataTable.to_excel('C:/Users/travismaekawa/Desktop/PythonCode', sheet_name="Loan.xlsx", index=False)
        print(dataTable)
    elif userInput == "3":
        loanTotal = float(loan)
        increase = input("How much more would you like to pay each month? ")
        payment = payment + float(increase)
        months = 0
        while loanTotal > 0:
            interest = (loanTotal * (r/12))
            principal = payment - interest
            loanTotal = loanTotal - principal
            months += 1
        numMonths = 12 * t
        numMonths = numMonths - months
        print("You will cut off " + str(numMonths) + " months off your loan.")
    elif userInput == "4":
        num = 12 * int(t)
        pHighMonth = 0
        for i in range(num - 1):
            p_check = loanDict["Principal"][i]
            i_check = loanDict["Interest"][i]
            pHighMonth += 1
            if p_check > i_check:
                print("Your principal is higher than your interest at month " + str(pHighMonth))
                break
    elif userInput == "5":
        num = 12 * int(t)
        totalPayment = payment * num
        print("The total that you will pay is $" + str(totalPayment))
        print("This is $" + str(totalPayment - int(loan)) + " more than the amount you borrowed")
    elif userInput == "6":
        print("Goodbye!")
        break




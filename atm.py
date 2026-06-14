def main():
    
    # getting user's Balance in float , let's introduce
    # string methods to ignore $ as well
    
    balance = input("Enter your Balance: ")
    balance = balance.replace("$", "")
    balance = float(balance)
    
    # withdraw_amount do the same as for balance
    
    withdraw_amount = input("Enter your withdraw_amount: ")
    withdraw_amount = withdraw_amount.replace("$", "")
    withdraw_amount = float(withdraw_amount)
    
    if withdraw_amount <= balance and withdraw_amount > 0 :
        balance -= withdraw_amount
        print(f"Approve , balance update:{balance}$")
    if withdraw_amount > balance:
        print("Insufficient Funds")
    if withdraw_amount <= 0 :
        print("Invalid")
        
    
    
    
    
    
main()
def create_account(accounts):
    acc_num = input("Enter account number: ")
    name = input("Enter Your Bank Account Name: ")
    deposit = float(input("Enter Deposit: "))
    acc_type = input("Enter account type: ")
    accounts[acc_num] = [name, deposit, acc_type]
    print("You registred succesfully!")
    
def perfom_transaction(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        print("1. Deposit")
        print("2. Withdraw")
        deposit_or_withdraw = input("You Want Deposit Or Withdraw?: ")
        amount = float(input("Enter amount: "))
        if deposit_or_withdraw == 1:
            accounts[acc_num][1] += amount
            print("amount is deposited successfullly thank you for credit!")
        elif deposit_or_withdraw == 2:
            if accounts[acc_num][1] >= amount:
                accounts[acc_num][1] -= amount
                print("Amount Withdraw successfully Done!")
            else:
                print("0 balance")
        else:
            print("invalid choice")
    else:
        print("Accpunt not found")
            
            
def update_account(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        name = input("please enter your new name: ")
        acc_type = input("Enter new account type: ")
        accounts[acc_num][0] = name
        accounts[acc_num][2] = acc_type
        print("Account information updated successfully")
    else:
        print("Account not found!!!")

def delete_account(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        del accounts[acc_num]
        print("Account deleted successfully!")
    else:
        print("Account not found!!!")
        
def search_acc_info(accounts):
    acc_num = input("Enter account number: ")
    if acc_num in accounts:
        print("Account number: ", acc_num)
        print("Name: ", accounts[acc_num][0])
        print("Balance: ". accounts[acc_num][1])
        print("Account type: ", accounts[acc_num][2])
    else:
        print("AMount undefind")
        
def view_customers_list(accounts):
    if accounts:
        for acc_num, details in accounts.item():
            print("Account Number: ", acc_num)
            print("Name: ", details[0])
            print("Balance: ", details[1])
            print("Account type: ", details[2])
            print()
    else:
        print("Accounts undefind")
        
def main():
    accounts = {}
    while True:
        print("\nDaniel Bank System")
        print("1. create account")
        print("2. perfom transaction")
        print("3. delete account")
        print("4. search account info")
        print("5. update account info")
        print("6. view customers list")
        print("7. exit system")
        choice = int(input("enter tour command: "))
        
        if choice == 1:
            create_account(accounts)
        elif choice == 2:
            perfom_transaction(accounts)
        elif choice == 3:
            delete_account(accounts)
        elif choice == 4:
            search_acc_info(accounts)
        elif choice == 5:
            update_account(accounts)
        elif choice == 6:
            view_customers_list(accounts)
        elif choice == 7:
            exit(accounts)
        else:
            print("invalid cjoice!!!")
if __name__ == "__main__":
    main()
class Bank_Account:
    
    def __init__(self,bank_id,balance=0):
        self.bank_id = bank_id
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            print(f"Deposited: Rs.{amount}")
        else:
            print("Invalid Deposit Amount")

    def withdrawl(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance-=amount
        else:
            print("Withdrawl Amount Invalid")

    def check_balance(self):
        print(f"Available Balance: {self.balance}")

    def quit(self):
        print("Have a great day! :)")

if __name__ == "__main__":
    id = input("Enter Bank ID:")
    bal = int(input("Enter balance:"))
    account = Bank_Account(id,bal)
    active = True 
    while active:
        print("-------------------------------------------------------------------")
        print("Select Operation \n[1]Deposit\n[2]Withdraw\n[3]Check Balance\n[4]Exit")
        option = int(input(":"))
        print("-------------------------------------------------------------------")
        if option == 1:
            amt = int(input("Enter amount to deposit:"))
            account.deposit(amt)
        elif option ==2:
            amt = int(input("Enter amount to withdraw:"))
            account.withdrawl(amt)
        elif option ==3:
            account.check_balance()
        elif option == 4:
            account.quit()
            active = False

class Account:
    def __init__(self,owner,balance=0): # owner and balance information
        self.owner = owner
        self.balance= balance
    
    def __str__(self):
        return f'Account owner:  {self.owner}\n Account balance: ${self.balance}' # put both account owner and balance information in string 
    
    def deposit(self,dep_amt):         # deposit information
        self.balance =+ dep_amt
        print(f'{dep_amt} has been debited into your account')
    
    def withdraw(self,wd_amt):  # withdrawal information
        if self.balance >= wd_amt:
            self.balance -= wd-amt
            return f'{wd_amt}has been deducted from your account and your balance is {balance}'
        else:
            return f'no sufficient fund in your account!'
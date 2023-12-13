class Bank:
    ac_num:int
    name:str
    ac_type:str
    ifsc_code:str
    branch:str
    balance:float

    def creat_account(self,ac_num,name,type,ifsc,branch,balance):
        self.ac_num=ac_num
        self.name=name
        self.ac_type=type
        self.ifsc_code=ifsc
        self.branch=branch
        self.balance=balance
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"your {self.ac_num} has been credited with {amount}, available balance is {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-amount
            print(f"your {self.ac_num} has been debited with {amount}, available balance is {self.balance}")

    def get_balance(self):
        print(f"your available balance is {self.balance}")


user1=Bank()
user1.creat_account(659844665,"nirupama","savings","SBIN0089412","kakkanad",2000)
user1.deposit(500)
user1.withdraw(1000)
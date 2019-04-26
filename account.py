class account:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.loan = 0
        self.balance = 0
        self.deposits = []
        self.withdrawal = []

    
    def welcome(self):  
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)

    def deposit(self,f):
        deposit = f
        self.balance=self.balance + f
        self.deposits.append(f)
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,f)


    def withdraw(self,y):
        withdraw=y
        if y > self.balance:
            return "not successful"
        else:
            self.balance=self.balance-y
            self.withdrawal.append(y)
            return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,y)

    def show_balance(self):
        showbalance=self.balance
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)

    def show_deposits(self):
        for f in self.deposits:
            print(f)    

    def show_withdrawal(self): 
        for g in self.withdrawal:
            print(g)

    def loan(self,amount):
        if len(self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
           self.loan=self.loan+amount
           print("dear, {} {} you can get a loan of {}".format(self.first_name,self.last_name,amount))
        else:
           print("dear, {} {} you cannot get a loan of {}".format(self.first_name,self.last_name))

    def pay_loan(self,amount):
        if self.loan==0:
           print("you dont have an existing loan")
        elif amount<self.loan:
           self.loan=self.loan-amount
           print("hello {} you have paid a part of your loan, {}. your remaining balance is {}".format(self.name, amount, self.loan))
        elif amount==self.loan:
           self.loan==self.loan-amount
           print("you have paid your existing loan")   
        elif amount>self.loan:
           more=amount-self.loan    
           self.balance= more-self.balance
           self.loan=amount-self.loan-more
           print("hello {} you have paid more than is necesssry, your new balance is{}".format(self.name,self_balance))

     
           


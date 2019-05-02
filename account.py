from datetime import datetime
class Account:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.loan = 0
        self.balance = 0
        self.deposits = []
        self.withdrawal = []

    
    def welcome(self):  
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)

    def deposit(self,amount):
        deposit = amount
        time = datetime.now()
        object={"time":time, "amount":amount}
        self.deposits.append(object)

        self.balance=self.balance + amount
    
        return "dear, {} {} your deposit of KES {}".format(self.first_name,self.last_name,amount)

    def withdraw(self,amount):
        withdraw = amount
        time = datetime.now()
        object={"time":time, "amount":amount}
        self.withdrawal.append(object)

        if amount > self.balance:
            return "not successful"
        else:
            self.balance=self.balance-amount
            
            return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,amount)

    def show_balance(self):
        showbalance=self.balance
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)

    def show_deposits(self):
        for deposit in self.deposits:
            time = deposit["time"]
            formatted_time=time.strftime("%c")
            deposit = deposit["deposit"]
            print("On {} you deposited {}".format(formatted_time,amount))

    def show_withdrawal(self): 
        for amount in self.withdrawal:
            time = amount["time"]
            formatted_time=time.strftime("%c")
            amount=withdraw["amount"]
            print("On {} you have withdrawn {}".format(formatted_time,amount))

    def give_loan(self,amount):
        loan = amount
        total = 0

        for a in self.deposits:
            deposit = deposit["deposit"]
            total+=deposit

        if len(self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
           self.loan=self.loan+amount
           print("dear, {} {} you can get a loan of {}".format(self.first_name,self.last_name,amount))
        else:
           print("dear, {} {} you cannot get a loan of {}".format(self.first_name,self.last_name))

    def pay_loan(self,amount):

        payment = amount

        self.loan.extend(amount)

        self.loan = self.loan - amount
        excess_payment = self.deposit.append(deposit)

        print("hello {} you have paid more than is necessary, your new balance is{}".format(self.first_name,self.balance))


        # if self.loan==0:
        #    print("you dont have an existing loan")
        # elif amount<self.loan:
        #    self.loan=self.loan-amount
        #    print("hello {} you have paid a part of your loan, {}. your remaining balance is {}".format(self.first_name, amount, self.loan))
        # elif amount==self.loan:
        #    self.loan==self.loan-amount
        #    print("you have paid your existing loan")   
        # elif amount>self.loan:
        #    more=amount-self.loan    
        #    self.balance= more-self.balance
        #    self.loan=amount-self.loan-more
        #    print("hello {} you have paid more than is necessary, your new balance is{}".format(self.first_name,self.balance))

     
           


import random as r
class loan_amount:
   
    def __init__(self,loan_amount):
        self.loan_amount= loan_amount
# what if i just want to initialize a variable but i dont want to pass it while ccalling a class .
    
    def update_loan_amoount(self,loan_emi):
        self.loan_amount =self.loan_amount-loan_emi

    def display_loan_amount(self):
        print(f"The Remaining Loan Amount is{self.loan_amount}")

    def get_fix_rate(self):
        self.base_rate = r.random()
        self.base = r.randint(5,7)
        self.total_interest=float(f"{((self.base+float(f"{self.base_rate:.2f}")+1.5)/100):.2}")
        
        return self.total_interest
        
    def display_interest_amount(self,a):
        self.Interest_amount = self.loan_amount * a
        print(f"This month Interest rate is {a} % and your Interest amount is {self.Interest_amount}")
        return self.Interest_amount

def check_taxable_amount(salary):
    if salary >= 100000:
        taxable_amouunt = salary*(20/100)
    elif salary>=50000:
        taxable_amouunt = salary*(10/100)
    elif salary>=25000:
        taxable_amouunt = salary*(5/100)
    elif salary>=12500:
        taxable_amouunt = salary*(2.5/100)
    else:
        taxable_amouunt= 0
    return taxable_amouunt
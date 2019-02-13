class Bank_acc(object):
    def __init__(self):
        self.name=""
        self.balance = 0
        self.pin = 1234
        self.intrate = 0.06
        self.acc_num = 123456789
    def credit_acc(self):
        ammount = float(input("enter your deposit"))
        self.balance+=ammount
    def debit_acc(self):
        get_pin = int(input("what is your pin"))
        if get_pin != self.pin:
            print("that is not correct the cops have been called")
        else:
            ammount = float(input("enter your withdraw amount"))
            self.balance -= ammount

cody_acc = Bank_acc()
cody_acc.name = "Cody"
print(cody_acc)
cody_acc.credit_acc()
print(cody_acc.balance)
cody_acc.debit_acc()
print(cody_acc.balance)

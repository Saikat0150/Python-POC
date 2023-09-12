class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8


b1 = Bank()
b2 = SBI()
b3 = ICICI()

print("Bank Rate of Interest: ", b1.getroi())
print("Bank Rate of Interest: ", b2.getroi())
print("Bank Rate of Interest: ", b3.getroi())

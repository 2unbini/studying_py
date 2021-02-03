#calculator.py

class Cal:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def add(self):
        return self.n1 + self.n2
    def sub(self):
        return self.n1 - self.n2
    def mul(self):
        return self.n1 * self.n2
    def div(self):
        return self.n1 / self.n2

class ZeroCal(Cal):
    def div(self):
        if self.n2 == 0:
            return 0
        else:
            return self.n1 / self.n2

class MoreCal(Cal):
    def squ(self):
        return self.n1 ** self.n2

class User:
    name = "Eunbin"
    age = 26
    now = "studying"
    language = "python"


a = Cal(5, 6)
b = ZeroCal(7, 0)
c = MoreCal(2, 10)
d = User()

A = a.sub()
B = b.div()
C = c.squ()
print(A+B+C)
print(d.now)
User.now = "sleeping"
print(d.now)

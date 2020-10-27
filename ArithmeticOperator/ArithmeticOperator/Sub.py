class Overload:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __sub__(self, other):
        s = Overload(0, 0)
        s.a = self.a - other.a
        s.b = self.b - other.b
        return s
     
    def display(self):
        print("Value of a = ", self.a, "  Value of b = ", self.b)
        return 
     
    pass

p1 = Overload(25, 20)
p2 = Overload(20, 4)
p3 = p1-p2
p3.display()
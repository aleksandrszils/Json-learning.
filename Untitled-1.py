class Prece:
    def __init__(self, item , price , quantity):
       self.item = item
       self.price = price
       self.quantity = quantity
       all = []
    def __init__(self, name:str, price:float, quantity:int = 0):
        assert prece > 0,  'kļuda cena nevarbūt negatīva!'
        assert quantity >= 0,  'kļuda cena nevarbūt negatīva!'

        self.name = name
        self.price = price
        self.quantity = quantity
        Prece.all.append(self)

    def change_quantity(count):
        self.quantity += count


p1 = Prece("Laptop", 650, 10)
p2 = Prece("Phone", 210, 5)
p3 = Prece("Toilet", 1000, 2)
p4 = Prece("Banknote",10, 1)
print(p1.name)
print(p3.quantity)
for prece in Prece.all:
    print(f"{prece.name}: {prece.model}, Price: {prece.price}, Quantity:{prece.quantity}")

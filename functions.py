def myfunction(name):
    print(name)

myfunction("Saman")


def totalCalculate(item,qty,price):
    print("The "+ item + " costs" , (qty*price), "rupees")

totalCalculate("Pizza",2,1500.00)

def totalCalculate(item,qty,price):
    return "The "+ item + " costs" , (qty*price), "rupees"

print (totalCalculate("Cake",4,1500.00))

print(totalCalculate(item="Apple(s)",qty=150,price=45))

def totalCalculateWithCurrency(item,qty,price, currency=" Rupees"):
    return "The "+ item + " costs " + str(qty*price) + currency

print(totalCalculateWithCurrency(item="Apple(s)",qty=150,price=45))
print(totalCalculateWithCurrency(item="Grapes",qty=100,price=5,currency=" $"))

def calculate(*values):
    print(sum(values))

calculate(1,3,4,5,1,4)
calculate(10,5,25)


def greeting(msg, *names):
    for name in names:
        print(msg + ", " + name)

greeting("Hello","Saman","Kamal","Sanath")

def calculateTotal(quantity, price):
    """Returns the product of quantity and price"""
    return quantity*price

print (calculateTotal.__doc__)
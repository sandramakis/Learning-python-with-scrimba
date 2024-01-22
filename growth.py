print('Welcome to Python 101')

# Datetypes and Typecasting- In JS(type conversion)
a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
c1 = int(float("3.4"))   # c1 will be...(3)
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,c1,d,e,f,g,h,i,j])

# Variables and datatypes- Excercise 
print('Variables & Datatypes - Exercise')
#Create appropriate Variables for Item name, the price 
#and how many you have in stock

item_name = "Sunglasses"
price = 5500
quantity_in_stock = 5
print('We have ' + item_name + " at N" + str(price) + " and just " + str(quantity_in_stock) + " pcs are left")


# Basic Arithmetic
k=10
l=3
print('Addition : ', k + l)
print('Subtraction : ', k - l)
print('Multiplication : ', k * l)
print('Division (float) : ', k / l)
print('Division (floor) : ', k // l)
print('Modulus : ', k % l)
print('Exponent : ', k ** l)
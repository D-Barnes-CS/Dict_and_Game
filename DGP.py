'''
Using turtle and random libraries
'''
import random
from random import randint
import turtle

dict = {}
orderID, customerID, count = 0, 0, 0
product = ["switch", "xbox", "playstation", "pc", "iphone", "android", "lotion", "chapstick"]
while count < 1000:
    orderID = randint(0, 9999)
    customerID = randint(0, 5555)
    d = f"{random.randint(2000, 2023)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
    choice = random.choice(product)
    dict[orderID] = {customerID, d, choice}
    count += 1

lst = [(key, value) for key, value in dict.items()]
tup = tuple(lst)

WINDOW = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

x, y = 0, 1000

for i in tup:
    barcode = hash(str(i))
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.write(f"Barcode: {barcode}\n", font=("Times New Roman", 16, "normal"))
    y -= 60

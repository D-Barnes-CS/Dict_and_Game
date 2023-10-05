'''
D Barnes
Revision 10/4/2023
HW4
'''
import random
'''
These are gonna be lists that I have pre-made data for and im going to insert them into 
a dictionary. then i'll allow the user to search through the dictionary with a given key 
or element in my list. 
'''
#P1
sample1 = ["barnesdy", "poop0987", "09/27/2000", "123 sesame st", "123-45-6789", "Pizza", "Tom"]
sample2 = ["johnsmith", "jonheal", "08/30/2000", "456 babysit st", "9876-54-321", "Corn", "Joe"]
sample3 = ["ethika", "costco65", "06/06/2003", "789 appletree st", "453-12-6789", "Cider", "Tom"]
user_records = [sample1, sample2, sample3]
user_data = {}

for ls in user_records:
    user_data[user_records.index(ls)] = ls

x = input("Would you like to search through the user data? (Y/N) ")
x = x.upper()
if x == 'Y':
    z = input("Do you know the ID? (Y/N) ")
    z = z.upper()
    if z == 'Y':
        w = int(input("What is the ID? "))
        print(user_data[w])
    elif z == 'N':
        y = input("What would you like to search for? ")
        for key, value in user_data.items():
            for ls in value:
                if ls == y:
                    #will print out all of the keys that contain that element. Try typing tom.
                    print("The ID(s) for your search are: " + str(key))
    else:
        print("Incorrect response.")
else:
    print("Goodbye")

#P2
'''
Guessing number game with pirates. If they guess the right number then they win some riches from a random
treasure chest. However if they guess the wrong number then the cursed chest takes money from them.
Chest comes with a set amount of funds and it can be increased and the user can win some money from it. 
'''
treasure = random.randint(0, 2000)
bank = random.randint(1, 150)
while (bank > 0):
    print("You have " + str(bank) + " in your pockets.")
    loot = random.randint(0, treasure)
    butt = random.randint(0, 300)
    #you have to give y or n AND your guessing number
    bet = input("Would you like to guess a number (0 - 300) for riches? (y/n) ")
    bet = bet.split()
    if bet[0].upper() == 'Y':
        wager = int(input("How much would you like to wager? "))
        if int(bet[1]) == butt:
            bank += loot
            treasure -= loot
        else:
            bank -= wager
            treasure += wager
        print("the number was " + str(butt))

    else:
        print("Goodbye")
        break

#P3

from random import *
from time import *

Opt1 = ["Melon", "Grape", "Cherry", "$$$", "Diamond", "7"]
Opt2 = ["Melon", "Grape", "Cherry", "$$$", "Diamond", "7"]
Opt3 = ["Melon", "Grape", "Cherry", "$$$", "Diamond", "7"]
money = 100

while money >=0:
    r1 = randint(0, 6)
    r2 = randint(0, 6)
    r3 = randint(0, 6)
    
    ONE = Opt1[r1%len(Opt1)]
    TWO = Opt2[r2%len(Opt2)]
    THREE = Opt3[r3%len(Opt3)]


    print("_______________________________")
    print()
    print("|", ONE, " | ", TWO, " | ", THREE, "|")
    print("_______________________________")

    if ONE == 7 and TWO == 7 and THREE == 7:
        print("Jackpot! You get 2 dollars! [...]AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print("You now have $"+ str(money))
        money += 2
        input()
    else:
        print("You lose 1 dollar... [...]")
        print("You now have $"+ str(money))
        money -= 1
        input()

print("u suk")

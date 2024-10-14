szam = int(input("Adjon meg egy számot: "))

if szam % 3 == 0 and szam % 4 == 0:
    print("A szám osztható 3-mal és 4-gyel is.")
elif szam % 3 == 0:
    print("A szám csak 3-mal osztható.")
elif szam % 4 == 0:
    print("A szám csak 4-gyel osztható.")
else:
    print("A szám sem 3-mal, sem 4-gyel nem osztható.")

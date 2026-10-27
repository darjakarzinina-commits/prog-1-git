#29.09

def rezervacija(skaits):
    if skaits <= 3:
        return "Rezervācija pieņemta"
    elif skaits == 0:
        return "Izvēlies vismaz vienu grāmatu"
    else:
        return "Vienā reizē drīkst rezervēt ne vairāk kā 3 grāmatas"

ievade = input("Cik grāmatas vēlies rezervēt? ")
skaits = int(ievade)
print(rezervacija(skaits))



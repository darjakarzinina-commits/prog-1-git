#13/09


def rezervacija(skaits):
    if skaits < 0:
         return "Nederīga ievade"
    elif skaits == 0:
        return "Izvēlies vismaz vienu grāmatu"
    elif skaits <= 3:
            return "Rezervācija pieņemta"
    else:
        return "Vienā reizē drīkst rezervēt ne vairāk kā 3 grāmatas"

ievade = input("Cik grāmatas vēlies rezervēt? ")
try:
  skaits = int(ievade)
  print(rezervacija(skaits))
except ValueError:
 print("Nederīga ievade")
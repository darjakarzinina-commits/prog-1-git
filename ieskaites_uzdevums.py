#13/09


def parbaudit_pieteikumus(skaits):
    if skaits <= 30:
        return "Pieteikšanās pieņemta"
    elif skaits == 0:
        return "Nav dalībnieku"
    else:
        return "Vietu nav"

ievade = input("Dalībnieku skaits: ")
skaits = int(ievade)
print(parbaudit_pieteikumus(skaits))


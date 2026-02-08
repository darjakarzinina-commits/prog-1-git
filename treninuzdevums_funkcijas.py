#08/02
#Treniņa uzdevums: Funkcijas Python valodā

"""Funkcijas prasības:
saņem sarakstu ar skolēnu vērtējumiem (skaitļi);

aprēķina:
vērtējumu skaitu,
vidējo vērtējumu,
augstāko vērtējumu;

nosaka teksta novērtējumu:
ja vidējais ≥ 7 → "labi"
ja vidējais ≥ 4 → "vidēji"
citādi → "jāuzlabo"

atgriež vārdnīcu (dictionary) ar rezultātiem."""

#aprēķina: 
#vērtējumu skaitu,
#vidējo vērtējumu,
#augstāko vērtējumu;

def analize_vertejumus(vertejumi):
    skaits = 0
    summa = 0
    augstakais = vertejumi[0]

    for v in vertejumi:
        skaits += 1
        summa += v
        if v > augstakais:
            augstakais = v

    videjais = summa / skaits  #mēklēju to internetā, jo nesapratu

#nosaka teksta novērtējumu:

    if videjais >= 7:
        vertejums = "labi"
    elif videjais >= 4:
        vertejums = "vidēji"
    else:
        vertejums = "jāuzlabo"

#vardnica ar rezultātiem

    rezultats = {
        "skaits": skaits,
        "videjais": videjais,
        "augstakais": augstakais,
        "vertejums": vertejums
    }

    return rezultats

#parbaude

vertejumi = [2, 7, 9, 4]
rezultats = analize_vertejumus(vertejumi)

print("Skaits:", rezultats["skaits"])
print("Vidējais:", rezultats["videjais"])
print("Augstakais:", rezultats["augstakais"])
print("Vērtējums:", rezultats["vertejums"])
        

#29/01

"""Izveido Python programmu, kas:

Pajautā lietotājam:

vārdu (string)

vecumu (number)

trīs iecienītākās krāsas (list)

Saglabā datus vārdnīcā (dictionary)

Izvada visu informāciju vienā print() komandā

📌 Atļauts izmantot tikai:

input

print

string, number, list, dictionary"""

#Izveido Python programmu, kas: Pajautā lietotājam:vārdu (string),vecumu (number),trīs iecienītākās krāsas (list)
skolens = {}
skolens["vards"] = input("Ievadi vārdu: ") 
skolens["vecums"] = int(input("Ievadi vecumu: "))


krasa = []
krasa.append(input("Ievadi 1. iecienītāko krāsu: "))
krasa.append(input("Ievadi 2. iecienītāko krāsu: "))
krasa.append(input("Ievadi 3. iecienītāko krāsu: "))

#Saglabā datus vārdnīcā (dictionary)
skolens["krasas"] = krasa


print("Dati:", skolens)








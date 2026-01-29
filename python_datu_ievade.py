#26.01.2026
#Datu ievade

#input()

#Svarigi: funkcija input() vienmer atgriež tekstu

vards = input("Ievadi savu vārdu:  ")
print(vards)

#skaitlis ievade
#Izmantot funkcijas int() un float()
skaitlis = float(input("Lūdzu ievadi savu mīļāko skaitli: "))
print("Tavs mīļakais skaitlis + 5 ir: ",skaitlis+5)

#Datu ievade un saglabāšana sarakstā

prieksmeti = []
prieksmeti.append(input("Ievadi 1. priekšmetu: ")) #ar metodi .append() pievienojam vērtību
prieksmeti.append(input("Ievadi 2. priekšmetu: "))

print("Tavi priekšmeti:", prieksmeti)

##Datu ievade un saglabāšana vārdnīca

skolens = {} #vārdnicas izveide
skolens["vards"] = input("Ievadi vārdu: ") #Izveidojam atslēgu pievienojam vērtību
skolens["vecums"] = int(input("Ievadi vecumu: "))

print("Skolēna dati:", skolens)


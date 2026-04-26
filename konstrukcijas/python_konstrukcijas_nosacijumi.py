#29/01

#Nosacījumi - if, else, elif

vecums = int(input("Ievadi savu vecumu: "))

if vecums >= 18: #Matemātiski salīdzinām
    print("Tu esi pilngadīgs.") #Izpildīts, ja nosacījums ir pareizs
else:
    print("Tu vēl neesi pilngadīgs.") #Izpildas, ja nosacījums ir nepareizs


#Piemērs ar tektu
vards = input("Ievadi savu vārdu: ")

if vards == "Anna": #Simbolu salīdzināšana izmantojam ==
    print("Sveika, Anna!")
else:
    print("Sveiki, lietotāj!")

    #if – elif – else struktūra
atzime = int(input("Ievadi atzīmi (1–10): "))

if atzime >= 9:
    print("Izcili!")
elif atzime >= 6:
    print("Ieskaite")
else:
    print("Nepietiekami")

   #Piemērs ar sarakstu (list)
augli = ["ābols", "banāns", "bumbieris"]

#1. variants
izvele = input("Ievadi augļa nosaukumu: ")

if izvele in augli:
    print("Šis auglis ir sarakstā.")
else:
    print("Šī augļa sarakstā nav.")

    #2. variants
    izvele = input("Ievadi augļa nosaukumu: ")

if izvele == "auglis" [0]:
    print("Šis auglis ir sarakstā.")
elif izvele == "auglis" [1]:
    print("Šis auglis ir sarakstā.")
elif izvele == "auglis" [2]:
    print("Šis auglis ir sarakstā.")
else:
    print("Šī augļa sarakstā nav.")

    #Nosacījumi ar vairākām pārbaudēm
lietotajvards = input("Ievadi lietotājvārdu: ")
parole = input("Ievadi paroli: ")

#1. variants
if lietotajvards == "admins" and parole == "1234": #AR loģisko operātoru and
    print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")

#2.variants
if lietotajvards == "admins": #AR nosacijumu (nesting)
    if parole == "1234":
     print("Piekļuve atļauta.")
else:
    print("Nepareizs lietotājvārds vai parole.")

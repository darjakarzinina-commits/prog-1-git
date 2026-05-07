#Datu saglabāšana datnē.mājasdards.py

pirmais_produkts = input("Ievadiet 1. produktu: ")
otrais_produkts = input("Ievadiet 2. produktu: ")
tresais_produkts = input("Ievadiet 3. produktu: ")

with open("produkti.txt","a", encoding="utf-8") as f:
 f.write(pirmais_produkts + "," + otrais_produkts + "," + tresais_produkts + "\n")
 
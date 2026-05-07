#30/04
#CSV datnes nolasīšana un datu apstrāde - uzdevums
skaits = 0 
#Izveido programmu, kas izvada tikai skolēnus no Jelgavas.
with open("students.csv", encoding="utf-8") as fails: 
    next(fails)
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  
        if pilseta == "Jelgava": 
            print(vards) 

#Izvada tikai tos skolēnus, kuri jaunāki par 17 gadiem.

vecums = input("Ievadi savu vecumu:")
print(vecums)
if vecums.isdigit():
    print("Ir skaitlis")
if vecums <= 17:
    print("Ir jaunāks par 17")
else:
    print("Nav jaunāks par 17")

#Saskaiti, cik ierakstu ir datnē.

skaits = 0 

with open("students.csv", encoding="utf-8") as fails: 
    next(fails)
    for rinda in fails:
     
     skaits += 1
print(skaits)

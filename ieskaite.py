

#3. uzd
with open("dati_ieskaite.csv", encoding="utf-8") as f:
    next(f)
    for rinda in f:
        vards,vecums = rinda.strip().split(",")  
        if float(vecums) >= 18:
            print(vards)

#3.1

#4.1 uzd

names = ["Laura", "Anna", "Marta", "Jānis"]
names.sort()
print(names)

#4.3

skaitli = [6,9,2,4,1]
skaitli.sort()
print(skaitli[:1])

5.1
names = ["Anna", "Laura", "Marta"]
meklet = input("Lūdzu ievadi vārdu, kuru vēlies atrast: ")
if meklet in names:
    print("Atrasts")
else:
    print("Nav atrasts")

5.3
with open("dati_ieskaite.csv", encoding="utf-8") as f:
     next(f)
     for rinda in f:
       vards, vecums = rinda.strip().split(",")

       if float(vecums) == 20:
          print(vards)


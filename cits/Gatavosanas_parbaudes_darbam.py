#14/05
#Gatavošanas noslēdzošajam parbaudes darbam

#1. uzdevums — Datu kvalitāte (6 p)
#1.1. Nosaki, kuri dati ir kvalitatīvi. Pamato. (4 p)
#Laura,17,Rīga
#???,-15,Mēness
#Jānis,18

#Piernie dati ir paši kvalitatīvākie, jo otrajā un trešaja piertukst informācijas vai tā ir neprecīza ar kļūdām

#1.2. Pārveido dotos nestrukturētos datus strukturētā tabulā. (2 p)
#“Marta dzīvo Jelgavā un viņai ir 16 gadi.”

#Marta, 16, Jelgava

#2. uzdevums — Datu validācija (8 p)
#2.1. Uzraksti programmu, kas pārbauda, vai ievadītais skaitlis ir robežās no 1 līdz 10. (5 p)
skaitlis = input("Lūdzu ievadi skaitli no 1-10:")
print(skaitlis)
if skaitlis.isdigit():
    print("Ir skailis")

    if 1 <= int(skaitlis) <= 10:
     print("Ir skaitlis no 1-10") 
    else:
        print("Nav skaitlis no 1-10")    
else:
 print("Nav skaitlis")

#2.2. Paskaidro, kāpēc validācija ir svarīga programmās. (3 p)
#Datu validācija ir vajadzīga, lai ievadīto datu pārbaudi pirms to izmantošanas.

#3. uzdevums — Datu apstrāde CSV failā (10 p)
#Dota datne:

#produkts,cena
#Piens,1.50
#Maize,2.00
#Sula,3.20
#Cepumi,4.50

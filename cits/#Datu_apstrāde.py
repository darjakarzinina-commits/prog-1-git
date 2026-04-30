#Datu apstrāde
#30/04


#Tikai vārdu izvadīšana
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        print(vards) #Izvada tikai vārdu
#Datu apstrādāšana - izvada tikai personas, kas dzīvo Rīgā
with open("students.csv", encoding="utf-8") as fails: #ar funkciju open() tiek atvērts csv fails,
    next(fails) #Funkcija next() izlaiž vienu rindu failā
    for rinda in fails:
        vards,uzvards,pilseta = rinda.strip().split(",")  #saglabājam datus mainīgajos, sadalot pēc atdalītāja
        if pilseta == "Rīga": #Pārbaude, vai pilsēta ir Rīga
            print(vards) #Izvada personas vārdu, kas dzīvo Rīgā
#30.01.2026
#Treniņa uzdevums: Nosacījumu struktūras Python valodā

#Izveido Python programmu, kas: Pieprasa lietotājam ievadīt:vārdu, vecumu, iecienītāko programmēšanas valodu

vards = input("Ievadi savu vārdu: ")
print("Sveiki, " + vards + "!")

#Programma: pārbauda, vai lietotājs ir pilngadīgs, pārbauda, vai ievadītā programmēšanas valoda ir sarakstā, izvada atbilstošu ziņojumu
vecums = int(input("Ievadi savu vecumu: "))

if vecums >= 18: 
    print("Tu esi pilngadīgs.") 
else:
    print("Tu vēl neesi pilngadīgs.")

iecienitaka_valoda  = input("Ievadi savu iecienītāko programmēšanas valodu: ")

programmesanas_valodas = ["Python", "Java", "C++", "JavaScript"]

if iecienitaka_valoda in programmesanas_valodas:
    print("Šī valoda ir sarakstā.")
else:
    print("Šī valoda sarakstā nav.")

#Kārtošanas algoritmi
#14/05/26

#Sakārtot skaitļs augošā secībā
skaitli = [5,1,8,7,9]
skaitli.sort() #Metode sort()sakātro datus augošā secībā
print(skaitli)

#Sakartot skaitļus dilstošā secībā
skaitli = [5,1,8,7,9]
skaitli.sort(reverse=True) #Metode sort(), izmantojot īpašību reverse, sakarto sarakstu dilstošā secībā
print(skaitli)

#Teksta kārtošana
vardi = ["Janis", "Anna", "Pēteris", "Darja"]
vardi.sort() #Metode sort()sakarto datus augošā secībā
print(vardi)

#Kārtošana csv faila datos
#Sakārtot atzīmes augošā secībā

gadiSaraksts = []
with open("students.csv", encoding="uft-8") as f:
    next(f)
    for rinda in f:
        vards, gadi, pilseta = rinda.strip().split(",")
        gadiSaraksts.append(int(gadi))
gadiSaraksts.sort()
print(gadiSaraksts)

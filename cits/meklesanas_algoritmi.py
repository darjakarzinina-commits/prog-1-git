#Meklēšanas algoritmi un datu atrašana
#14/05/26

#Pārbaudam vai dati eksistē, kur tie atrodas, vai tektā ir noteiktā daļa
vardi = ["Janis", "Anna", "Pēteris", "Darja"]
meklet = input("Lūdzu ievadi vārdu, kuru vēlies atrast: ")
if meklet in vardi:
    print("Atrasts")
else:
    print("Nav atrasts")

    #Datu meklēšana csv faila. Pārbaudīt vai faila ir konkrēts students
    meklet = input("Lūdzu ievadi vārdu,kuru vēlies atrast: ")
    atrasts = False #boolen tipa mainīgais, kas apzīme karodzņvērtību - vai mūsu nasacījums ir izpildīts, vai nē

    with open("students.csv", encoding="uft-8") as f:
     next(f)
    for rinda in f:
       vards, gadi, pilseta = rinda.strip().split(",")

       if meklet == vards: #Mēklējam, vai lietotāja ievadītais vārds it failā
          print("Atrasts")
          atrasts = True

       if not atrasts: #atrasts == False
          print("Nav atrasts")
         




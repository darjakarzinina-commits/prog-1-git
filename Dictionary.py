#26.01.202
#Python datu tips: Dictionary

#saraksts - []
#bibliotekai - {}

#Izveido vārdnīcu par sevi (iekļauj: vārds, vecums un iegūtā izglītība (pamatskolas, vidusskolas, augstākā un t.t.))

informacija = {"vards":"Darja",
            "vecums":16,
               "izglitiba":"pamatskola"
               }

#Izvadi izveidoto vārdnīcu
print(informacija)

#Izvadi vārdnīcas atslēgas
print(informacija.keys())

#Izvadi vārdnīcas atslēgu vērtības
print(informacija.values())

#Iedomājies, ka jau esi nosvinējis dzimšanas dienu un maini vērtību atslēgā vecums
informacija["vecums"] = 20

print(informacija)

#Izvadi tikai atslēgas vecums vērtību
print(informacija["vecums"])

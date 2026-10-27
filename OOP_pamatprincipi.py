#27/10/26

#OOP pamatprincipi
#objekts
#objekta īpašības
#klase, kas ir objekta veidne (templete)

#objekts - automasina
#īpašības: marka, modelis, krāsa un ātrums

class Automasina: #objekta nosaukumu vienmēr sāksim ar lielu burtu
    def __init__ (self, marka, modelis, krasa): #īpašību definēšana
        self.marka = marka
        self.modelis = modelis
        self.krasa = krasa
    #īpašība ar noklusējuma vērtību
        self.atrums = 0 

#pirmā objekta automašīna izveide
mansAuto = Automasina("Audi","A6","pelēka")
print(mansAuto.marka)
print(mansAuto.modelis)
print(mansAuto.krasa)
print(mansAuto.atrums)

mansAuto.atrums = 50
print(mansAuto.atrums)

#otra objekta automašīna izveide
tavsAuto = Automasina("Ford","Ranger","melna")
print(mansAuto.marka)
print(mansAuto.modelis)
print(mansAuto.krasa)
print(mansAuto.atrums)

tavsAuto.atrums = 110
print("Tavs Auto ātrums",tavsAuto.atrums)
print("Mans Auto ātrums",mansAuto.atrums)

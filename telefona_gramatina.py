#27/10/26

class kontakts:
    def __init__(self, vards, uzvards, talrunis):
        self.vards = vards
        self.uzvards = uzvards
        self.talrunis = talrunis


kontakts_1 = kontakts("Sabīne","Bērziņa","20965723")
print(kontakts_1.vards)
print(kontakts_1.uzvards)
print(kontakts_1.talrunis)

kontakts_2 = kontakts("Nika","Auziņa","20320894")
print(kontakts_1.vards)
print(kontakts_1.uzvards)
print(kontakts_1.talrunis)

kontakts_1.talrunis = 26999999
print("Kontakt info. 1.:", kontakts_1)
print("Kontakt info. 2.:", kontakts_1)



        
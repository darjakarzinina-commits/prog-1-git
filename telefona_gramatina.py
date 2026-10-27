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
print(kontakts_1.vards, kontakts_1.uzvards, kontakts_1.talrunis)
print(kontakts_2.vards, kontakts_2.uzvards, kontakts_2.talrunis)



        
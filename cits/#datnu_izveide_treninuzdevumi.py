#datnu_izveide_treninuzdevumi.py
#07/05/26

#1.Izveido failu vardi.txt, kur saglabāti 3 vārdi katrs jaunā rindā.
with open("vardi.txt", "w",encoding="utf-8") as f:
 f.write("Darja\n")
 f.write("Nika\n")
 f.write("Sabīne\n")

#2.Izveido CSV failu klase.csv
with open("klase.csv","w",encoding="utf-8") as f:
    f.write("vards,atzime\n")
    f.write("Elina,7\n")
    f.write("Engelina,10\n")
    f.write("Linda,3\n")
with open("klase.csv","a",encoding="utf-8") as f: #3.Papildini klase.csv ar vēl vienu skolēnu.
    f.write("Adriana,8\n")



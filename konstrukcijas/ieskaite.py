#02.03
vards = "Darja"
print("Sveiks",vards,"!")

age = int(input("Ievadi vecumu: "))

if age < 18:

 print("Nepilngadīgs")


def laukums(platums, garums):
    return platums*garums
rezultats = laukums(2,4)
print(rezultats)


skaitlis1 = int(input("ievadi pirmo skaitli:"))
skaitlis2 = int(input("ievadi otro skaitli:"))
summa = skaitlis1+skaitlis2
print(summa)
if summa > 100:
 print("Liels rezulāts")
elif summa <= 100:
   print("Mazs rezultāts")
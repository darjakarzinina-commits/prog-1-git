#02/02
#Treniņa uzdevums: Python cikls for

#1. uzdevums – skaitļi

#Izmanto ciklu for, lai: 
# #izvadītu visus skaitļus no 1 līdz 10
for i in range(10):
    print(i)

#izvadītu tikai pāra skaitļus
for i in range(1, 11):
    if i % 2 == 0: 
        print(i, "ir pāra skaitlis")

#2. uzdevums – teksts (string)

#Dots teksts:
text = "Programmēšana"

#Izmanto ciklu for, lai:
#izvadītu katru burtu jaunā rindā
for x in text:
    print(x)

#saskaitītu, cik burtu ir tekstā

summa = sum(1 for x in text)  #nesapratu kā šo izdarīt, meklēju internetā
print("Burtu skaits:", summa)

#3. uzdevums – saraksts (list)
#Dots saraksts:
numbers = [4, 7, 2, 9, 12]
 
#Izmanto ciklu for, lai:
#izvadītu katru skaitli
for number in numbers:
    print(number)

#izvadītu tikai tos skaitļus, kas ir lielāki par 5
for number in numbers:
    if number > 5:
        print(number)

#4. uzdevums – vārdnīca (dictionary)

#Dots vārdnīcas objekts:
student = {
"vārds": "Jānis",
"vecums": 17,
"kurss": "Programmēšana I"
}
 
#izmanto ciklu for, lai: izvadītu katru atslēgu un tās vērtību šādā formātā:
#vārds : Jānis
#vecums : 17
#kurss : Programmēšana I

print(student.items())
for key, value in student.items():
    print(key, ":", value)


# 5. uzdevums – papildus (⭐)
#Izmanto ciklu for, lai:

#saskaitītu visu saraksta numbers skaitļu summu
summaa = sum(numbers)

#izvadītu rezultātu
print("Skaitļu summa:", summaa)
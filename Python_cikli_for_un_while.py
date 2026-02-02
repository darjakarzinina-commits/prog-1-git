#02/02
#Python cikli: for un while

 #cikls - for

#for - ja ir zināms, cik reižu vai pa kādiem elementiem jāatkārto darbība

#📌 for ar skaitļiem (number)#range() - ļauj apstrādāt diapazonu
for i in range(5):
    print(i)

#📌 for ar tekstu (string)
text = "Python"

for letter in text:
    print(letter)

#📌 for ar sarakstu (list)
numbers = [3, 7, 2, 9]

for n in numbers:
    print(n * 2)

    #📌 for ar vārdnīcu (dictionary)
student = {
    "vārds": "Anna",
    "vecums": 16,
    "kurss": "Programmēšana"
}
print(student.items())
for key, value in student.items():
    print(key, ":", value)

#📌 for ar nosacījumu
print(2%2)
print(9%2)
for i in range(1, 11):
    if i % 2 == 0: #% - dalījums bez atlikuma
        print(i, "ir pāra skaitlis")
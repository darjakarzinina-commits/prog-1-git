#15/01/2026

#viena rinda
"""
vairāku rindu
komentārs
"""

# Teksts komentāra automātiski - ctrl+k+c

#Python datu tipi: Numbers un string

#numbers - skaitļi

skaitlis1 = 10 #int-vesels skaitlis
skaitlis2 = 5.5 #float-decimālskaitlis
#funkcija print()
print(skaitlis1)
print(skaitlis2)

darbiba1 = skaitlis2+skaitlis1 #float
print(darbiba1)
print(skaitlis1-skaitlis2)
print(skaitlis1*skaitlis2)
print(skaitlis1/skaitlis2)

# string - teksts, simbolu virkne

# define teksta mainīgos
teksts1 = "5"
teksts2 ="gadi"

#izvadīt atseviški un kopā
print(teksts1)
print(teksts2)

#teksta savienošana (+ un ,)
print(teksts1+teksts2)
print(teksts1+" "+teksts2)
print(teksts1,teksts2)

#simbolu sakits
print(len(teksts1)) #funkcija len
print(len(teksts2))


#izvadīt 1 teksta simbolu
print(teksts2[0])

#izvadīt 2 un 3 teksta simbolu
print(teksts2[1:3]) #3=i 1,2

#apgriez tekstu otrādāk
print(teksts2[::-1])

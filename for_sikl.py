# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:57:31 2021

@author: Asadbek
"""

ismlar = ['Ali', 'Vali', 'Gani', 'Botir', 'Begzod', 'Javoxir']

for name in ismlar:
    print(f' Salom {name}, yaxshimisan?')
print(f' Kod {len(ismlar)} marta takrorlandi')

sonlar = list(range(11, 100, 2))
for num in sonlar:
    print(num**3)


print(sonlar)
#print(11*11*11)

kinolar = []

for n in range(0,5):
   # kinolar.append(input(f'{n+1}-sevimli kino nomini kiriting:'))
    print(kinolar)
    
count = int(input('nechta odam bn suhbat qildingiz?>>>'))
people = []
#print(input(f'{3+5}'))
for nth in range(count):
    people.append(input(f"{nth+1}-suhbatlashgan odamingiz: "))
print(people)    
    

    
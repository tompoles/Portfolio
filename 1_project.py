'''
author = Tomas Polacek @tompoles
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

# 1. step - gr. user
oddelovac= '='*40
oddelovac_2= '-'*40
cislo_textu= (1,2,3)
print(oddelovac)
print('Vita vas Textovy analyzator v1.0')
print(oddelovac)
# user's data
users= {
        'novak':'1234',
        'poles':'nikon',
        'jana' :'5432',
        'rozi' :'spokojenec'
        }
# user's log in
pokracovat = 0
while pokracovat < 2:
    user = input('Zadejte sve prihlasovaci jmeno: ')
    password = input('Vlozte heslo: ')
    if users.get(user) == password:
        print('Pokracuji...')
        pokracovat = 3
        break
    else:
        print('Uzivatelske jmeno nebo heslo se neshoduje, zadejte znovu')
        pokracovat +=1
    quit(pokracovat > 3)
print(oddelovac)

# selection from list
user_choice=int(input(f'''Nahrane jsou celkem {len(TEXTS)}  textove soubory,
Vyberte jednu z moznosti (1,2 nebo 3): '''))
spravny_text = TEXTS[user_choice -1]
print(oddelovac)
print(spravny_text)
print(oddelovac)

# word count
word_count=spravny_text.split()
print(f'Ve Vami zvolenem textu je celkem {len(word_count)} slov.')
print(oddelovac)

# titlecase words
velka = 0
for vel in word_count:
    if vel.istitle():
        velka += 1
print(f'''Ve Vami zvolenem textu je celkem {velka} slov,
      ktere zacinaji velkym pismenem.''')
print(oddelovac_2)

# uppercase words
velka2 = 0
for vel2 in word_count:
    if vel2.isupper():
        velka2 += 1
print(f'''Ve Vami zvolenem textu je celkem {velka2} slov,
      ktere jsou napsany velkym pismenem.''')
print(oddelovac_2)

# lowercase words
lower = 0
for low in word_count:
    if low.islower():
        lower +=1
print(f'''Ve Vami zvolenem textu je celkem {lower} slov,
      ktere jsou napsany malym pismenem.''')
print(oddelovac_2)

# number of digits
numeric = 0
for num in word_count:
    if num.isnumeric():
        numeric += 1
        type(numeric)
print(f'''Ve Vami zvolenem textu je celkem {numeric} 
      ciselnych stringu.''')
print(oddelovac)

# bar chart
print('Histogram cetnosti - delka : slovo')
print(oddelovac_2)
cisty_text = [slovo.strip('.,') for slovo in word_count]
cislo= [len(slovo) for slovo in cisty_text]
pocet = {x:cislo.count(x) for x in cislo}
nejcastejsi_delka = sorted(pocet, key=pocet.get, reverse=False)[:]

for num, hodnota in enumerate(range(len(pocet), 0, -1), 1):
    for index in nejcastejsi_delka:
        velikost = index
        print(f"{index}: {pocet[index]*'*'} {pocet[index]}")
        nejcastejsi_delka.remove(index)
        break
print(oddelovac)

# # Sum of all digits
result = []
for digit in cisty_text:
    if digit.isdigit():
        digit = int(digit)
        result.append(digit)
digit = sum(result)
print(f'''Ve Vami zvolenem textu je soucet vsech 
        cisel roven: {digit}.''')
print(oddelovac)
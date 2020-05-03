'''
author = Tomas Polacek
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
oddelovac = '='*40
print(oddelovac)
print('Vita vas Textovy analyzator v1.0')
print(oddelovac)
# user's data
users = {
        'novak':'1234',
        'poles':'nikon',
        'jana' :'5432',
        'rozi' :'spokojenec'
        }

pokracovat = 0
while pokracovat < 3:
    user = input('Zadejte sve prihlasovaci jmeno: ')
    password = input('Vlozte heslo: ')
    if users.get(user) == password:
        print('Pokracuji...')
        break
    else:
        print('Uzivatelske jmeno nebo heslo se neshoduje, zadejte znovu')
        pokracovat += 1
print(oddelovac)
# selection from list
user_choice = int(input(f'''Nahrane jsou celkem {len(TEXTS)} textove soubory,
Vyberte jednu z moznosti (1,2 nebo 3): '''))
user_choice = TEXTS[-1]
print(oddelovac)
print(user_choice)
print(oddelovac)
# word count
word_count = user_choice.split()
print(f'Ve Vami zlovenem textu je celkem {len(word_count)} slov')
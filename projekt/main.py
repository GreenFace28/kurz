"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Vlach
email: mvlach@seznam.cz
"""
# text
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

# pomocné proměnné
cara = "-" * 35
# registrovaní uživatelé
users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# přihlášení
username = input("username: ")
password = input("password: ")
print(cara)
if username in users and password == users.get(username):
    print("Vítej v aplikaci, " + username + "\nMáš 3 texty na analízu. ")
else:
    print("Neregistrovaný uživatel, ukončuji program.")
    quit()
print(cara)

# zadaní čísla textu
zadání_textu = int(input("Zadej číslo textu 1 až 3: "))
print(cara)
if 1<= zadání_textu <=3:
    text_číslo = TEXTS[zadání_textu - 1]
else:
    print("Text neexistuje")
    quit()

# počet slov
slova = text_číslo.split()
počet_slov = len(slova)

# počet slov s velkým písmenem
s_velkym_pismenem ={"velkým písmenem": 0}
for velké_písmeno in slova:
    if velké_písmeno[0].isupper():
        if not velké_písmeno[1].isupper():
            s_velkym_pismenem["velkým písmenem"] +=1

# počet slov psané velkými písmeny
velkými_písmeny = {"slovo velkými písmeny": 0}
for velke_slovo in slova:
    if velke_slovo[:].isupper():
        velkými_písmeny["slovo velkými písmeny"] +=1

# počet slov malými písmeny
malá_slova = {"slova malými písmeny": 0}
for malé in slova:
    if malé.islower():
        malá_slova["slova malými písmeny"] +=1

# počet čísel
cisla = {"počet čísel": 0}
for cislo in slova:
    if cislo.isnumeric():
        cisla["počet čísel"] +=1

# suma čísel
cislo = ""
suma = 0
for znak in slova:
    if znak.isdigit():
        cislo += znak
    else:
        if cislo:
            suma += int(cislo)
            cislo = ""
if cislo != "":
    suma += int(cislo)

# statistika slov

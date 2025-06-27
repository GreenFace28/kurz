# zadání
mesta = ["Praha" , "Viden" , "Olomouc" , "Svitavy" , "Zlín" , "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
slevy = ("Olomouc", "Svitavy", "Ostrava")
domeny = ("gmail.com", "seznam.cz", "email.cz")

dvojita_cara = "=" * 35
cara = "-" * 35

nabidka = """
1 - Praha   | 150,-Kč
2 - Viden   | 200,-Kč
3 - Olomouc | 120,-Kč
4 - Svitavy | 120,-Kč
5 - Zlin    | 100,-Kč
6 - Ostrava | 180,-Kč
"""
rok = 2025

# přivítaní
print("Vítejte v naší aplikaci Destinatio")
print(dvojita_cara)

print(nabidka)
print(dvojita_cara)

# výber destinace
destinace = int(input("Vyber číslo destinace:"))

if 1<= destinace <= 6:
    destinace_nazev = mesta[destinace - 1]
    print("Destinace: ", destinace_nazev.upper())
else:
    print("Destinace", str(destinace), "neexistuje!!")
    quit()
print(cara)

# přepočet slevy
if destinace in slevy:
    nova_cena = 0.75 * ceny[destinace - 1]
    print("Získáváte 25% slevu. Výsledná cena: " + str(nova_cena) + ",-")
else:
    nova_cena = ceny[destinace - 1]
    print("Jízdenka bez slevy. Cena: " + str(nova_cena) + ",-")
print(cara)

#jmeno
cele_jmeno = input("Zadej svoje jméno a přijmení:")
krestni_jmeno = cele_jmeno.split()[0]
if krestni_jmeno.isalpha():
    print("Křestní jméno: ", krestni_jmeno)
else:
    print("Neplatné jméno!!")
print(cara)

#kontrola věku
vek = int(input("Zadej rok narození: "))
if (rok - vek) >= 18:
    print("V pořádku, pokračuj v objednávce.")
else:
    print("Tato aplikace je až od 18ti.")
    quit()
print(cara)

#ověření mailu
email = input("Zadej email: ")
if "@" in email and email.split("@")[1] in domeny:
    print("Ověření emailu je v pořádku")
else:
    print("Email je neplatný!!")
    quit()
print(dvojita_cara)

# výsledný výstup
print("" \
"\nDěkuji, " +  krestni_jmeno + " za objednávku jízdenky." +
"\nCílová destinace: " + destinace_nazev + " , cena jízdenky: " + str(nova_cena) + ",-" +
"\nNa vas email " + email + "jsme zaslali e-jizdenku\n"
)
print(dvojita_cara * 2)
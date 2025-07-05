samohlasky = 'aeiouáéíóúů'
souhlasky = 'bcčdďfghjklmnňpqrřsštťvwxzž'

vysledky = {'samohlasky': 0, 'souhlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'

for znak in veta:
    if znak.isalpha():
        znak = znak.lower()
        if znak in samohlasky:
            vysledky['samohlasky'] += 1
        elif znak in souhlasky:
            vysledky['souhlasky'] += 1

print(vysledky)

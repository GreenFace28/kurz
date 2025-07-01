jmeno = "Marek"
heslo = "12364"
uzivatel = {"Marek": "1234"}
zprava = ()

if jmeno in uzivatel and heslo in uzivatel.get("Marek"):
  zprava = "Ahoj Marek, vítej v aplikaci! Pokračuj..."
else:
  zprava = "Uživatelské jméno nebo heslo nejsou v pořádku!"

print(zprava)
  
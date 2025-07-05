# vstupní údaje 
oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}
# spojení slovníku film 1, 2, 3, 4 do jednoho
filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4,
}

# prihlaseni
uzivatel = input("Zadej jméno: ").lower()

if uzivatel in uzivatele:
    print("Si registrovaný")
else:
    print("Nejsi registrovaný, ukončuji program")
    quit()

print(oddelovac)
print("vitejte v nasem filmovem slovniku".upper().center(62),oddelovac, sep="\n")
print(("| " + " | ".join(sluzby) + " |").center(62), oddelovac, sep="\n" )

# vyber služby
vyber_sluzby = input("Vyber si službu: ").lower()
if vyber_sluzby in sluzby and vyber_sluzby == "dostupne filmy":
    print("Naše filmy :", ",".join(tuple(filmy.keys())), oddelovac, sep="\n")
elif vyber_sluzby in sluzby and vyber_sluzby == "detaily filmu":
    print("Naše filmy :", ",".join(tuple(filmy.keys())), oddelovac, sep="\n")
    vyber_filmu = input("Vyber si film o kterém chceš informace: ")
    print(oddelovac, "Film: " + vyber_filmu,  filmy.get(vyber_filmu, "Takový film nemáme!"), oddelovac, sep="\n")
elif vyber_sluzby in sluzby and vyber_sluzby == "reziseri":
    reziseri = {filmy["Shawshank Redemption"]["REZISER"],
                filmy["The Godfather"]["REZISER"],
                filmy["The Dark Knight"]["REZISER"],
                filmy["The Prestige"]["REZISER"]}
    print(", ".join(reziseri), oddelovac, sep="\n")
elif vyber_sluzby in sluzby and vyber_sluzby == "doporuc film":
    
else:
    print("Služba není v nabídce, ukončuji program!")
    quit()
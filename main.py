from text import *
ODDELOVAC = "=" * 80
user_dict = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
pocet_pokusu = 3
uzivatel = input(str("Zadej sve jmeno: "))

status = True

"""OVERENI TOTOZNOSTI"""

while status:

    if uzivatel in user_dict.keys():
        print(f"Ahoj {uzivatel.upper()}.")
        updated_dict = user_dict[uzivatel]

        heslo = input(str("Zadej sve heslo: "))

        if heslo != updated_dict:
            pocet_pokusu = pocet_pokusu - 1
            print(f"Zadal/a jsi špatné heslo. Zbývají ti {pocet_pokusu} pokusy.")

            if pocet_pokusu == 0:
                print("Vycerpal si vsechny pokusy.")
                status = False
            else:
                continue

        elif heslo == updated_dict:
            print("Správné heslo. Vítáme tě.")
            break

    else:
        print("Bohuzel nejsi registrovany uzivatel. Ukoncuji program.")
        status = False
        quit()

print(ODDELOVAC)

"""VYBER ANALYZOVANEHO TEXTU"""

vyber_textu = input("Vyber si, ktery text chces analyzovat (1,2,3): ")


if not vyber_textu.isnumeric():
    print("Zadaná hodnota není číslo. Ukončuji program.")
    quit()

elif vyber_textu > str(3):
    print("Takové číslo není v zadání. Ukončuji program.")
    quit()

else:
    vyber = int(vyber_textu) - 1
    spravny_vyber = TEXTS[vyber]

print(ODDELOVAC)

"""LIST SLOV"""

list_slov = spravny_vyber.split()

"""CISTA SLOVA"""

cista_slova = [slovo.strip(",.") for slovo in list_slov]

"""POCET SLOV"""

pocet_slov = len(cista_slova)
print(f"Počet slov ve vybraném textu je: {pocet_slov}.")


"""POCET SLOV ZACINAJICI VELKYM PISMENEM"""


velka_pismena = 0

for slovo in cista_slova:
    if slovo.istitle():
        velka_pismena += 1
    else:
        continue


print(f"Pocet slov zacinajici velkym pismenem: {velka_pismena}.")

"""POCET SLOV PSANYCH VELKYMI PISMENY"""

velka_slova = 0

for slovo in cista_slova:
    if slovo.isalpha() and slovo.isupper():
        velka_slova += 1

    else:
        continue

print(f"Pocet slov psanych velkymi pismeny je: {velka_slova}.")

"""POCET SLOV PSANYCH MALYMI PISMENY"""


mala_slova = 0

for slovo in cista_slova:
    if slovo.isalpha() and slovo.islower():
        mala_slova += 1
    else:
        continue

print(f"Pocet slov psanych malymi pismeny je: {mala_slova}.")

"""POCET CISEL"""

pocet_cisel = 0

for slovo in cista_slova:
    if slovo.isnumeric():
        pocet_cisel += 1
    else:
        continue

print(f"Pocet cisel je: {pocet_cisel}.")

"""LIST CISEL"""

list_cisel = []

for slovo in cista_slova:
    if slovo.isnumeric():
        list_cisel.append(int(slovo))
    else:
        continue

"""SUMA VSECH CISEL"""

for cislo in list_cisel:
    suma_cisel = sum(list_cisel)

print(f"Suma vsech cisel je: {suma_cisel}.")

print(ODDELOVAC)

print("POCET ZNAKU SLOVA | POCET VYSKYTU")


"""POČET OPAKOVÁNÍ"""

word_count = []

for slovo in cista_slova:
    delka_slova = len(slovo)
    word_count.append(delka_slova)

cetnost = {}

for cislo in word_count:
    if cislo in cetnost:
        cetnost[cislo] += 1
        continue
    else:
        cetnost[cislo] = 1


for index, _ in enumerate(range(len(cetnost), 0, -1), 1):
    print(ODDELOVAC)
    for item in sorted(cetnost):
        print(f"Pocet znaku: *{item}*, Vyskyt: {cetnost[item]}x")
    break



def pocet_hvezdicek(cislo: int):
    if cislo >= 1:
        cislo = (cislo * "*")
    else:
        quit()
    return cislo




"""Tento modul obsahuje hlavní funkce."""
import random
import os
import sys
import getpass
import time


def deslabikace(VstupniText):
    """
    Hlavní funkce programu.

    Na vstupu má uživatelem zadaný text a na výstupu rozházený text.
    Obsahuje vnořenou funkci mixer, která se stará o zpřeházení písmen
    v jednotlivých slovech.
    Příklady:
    >>> deslabikace("a")
    'a'
    >>> deslabikace("ab")
    'ab'
    >>> deslabikace("abc")
    'abc'
    >>> deslabikace("abcd")
    'acbd'
    >>> deslabikace("***Zdar***")
    '***Zadr***'
    >>> deslabikace("-4()*/abcd845")
    '-4()*/acbd845'
    >>> deslabikace("123456")
    Traceback (most recent call last):
        ...
    ValueError: Zadání neobsahuje žádná písmena!.
    >>> deslabikace("")
    Traceback (most recent call last):
        ...
    ValueError: Zadání neobsahuje žádná písmena!.
    """
    Deslabikovano = []

    def mixer(slovo):
        """
        Funkce pro promýchání písmen, která se použije pro slova delší než 4 \
        znaky.

        Kontroluje, jestli nejsou před prvním písmenem ještě nějaké jiné \
        znaky (např. uvozovky nebo závorky), a to stejné se kontroluje i od \
        konce. Vytvoří se množina znaků na začátku slova, která se nemění, \
        prostředek, který se promýchá a opět množina na konci slova, která se \
        nemění.
        PŘÍKLAD:
        >>> mixer("***Ahoj***")
        [['*', '*', '*', 'A'], 'o', 'h', ['j', '*', '*', '*']]
        """
        index_Z = 1  # začátek prohazované části
        index_K = -1  # konec prohazované části

        # tento cyklus zjistí, kde začínají písmena
        for i in range(len(slovo)):
            if not slovo[i].isalpha():
                index_Z += 1
            else:
                break

        # tento cyklus zjistí, kde končí písmena
        for i, item in enumerate(reversed(slovo)):
            if not (item.isalpha()):
                index_K -= 1
            else:
                break

        # Vybere všechny "prostřední" prvky určené pro zamýchání
        prostredek = slovo[index_Z:index_K]

        # Zamíchá prostřední část seznamu
        random.shuffle(prostredek)

        # Spojí první písmeno, zamíchanou prostřední část a poslední písmeno
        return [slovo[:index_Z]] + prostredek + [slovo[index_K:]]

    JednotlivaSlova = VstupniText.split()  # Rozdělení textu na list slov

    # Kontrolujeme, jestli zadaný řetězec obsahuje písmena
    if not any(znak.isalpha() for znak in VstupniText):
        raise ValueError("Zadání neobsahuje žádná písmena!")

    else:
        # Cyklus projede a zpracuje všechna slova v listu
        for i in range(len(JednotlivaSlova)):
            # Pokud slovo obsahuje tři nebo méně písmen, nic se nemění
            if len(JednotlivaSlova[i]) <= 3:
                Deslabikovano.append(JednotlivaSlova[i])

            # Pokud slovo obsahuje čtyři písmena, první a poslední se nemění a
            # prostředek prohodíme
            elif len(JednotlivaSlova[i]) == 4:
                Deslabikovano.append(JednotlivaSlova[i][0] +
                                     JednotlivaSlova[i][2] +
                                     JednotlivaSlova[i][1] +
                                     JednotlivaSlova[i][3])

            else:  # U delších slov se písmena náhodně promíchají
                while True:
                    # Udělá se list z písmen slova
                    pismena = list(JednotlivaSlova[i])

                    # Algoritmus proháže písmena
                    PrehazenaPismena = mixer(pismena)

                    # spojí položky seznamu (včetně dalších seznamů) do seznamu
                    PrehazeneSlovo = ''.join(''.join(vnitrek) for vnitrek
                                             in PrehazenaPismena)

                    # Podmínka kontroluje, jestli došlo k přeházení a
                    # nevzniklo nám náhodou stejné slovo, jako bylo na vstupu
                    if PrehazeneSlovo != JednotlivaSlova[i]:
                        break

                # Nakonec se upravené slovo přidá do listu
                Deslabikovano.append(PrehazeneSlovo)

    return (" ".join(Deslabikovano))


def cls():
    """Funkce pro vyčištění textu na obrazovce."""
    if os.name == "nt":
        prikaz = "cls"  # Windows
        os.system(prikaz)
    elif os.name == "posix":
        prikaz = "clear"  # Linux
        os.system(prikaz)
    else:
        # pokud není systém rozpoznán, jenom odřádkuje
        print("\n\n\n\n")


def NactiSoubor():
    """Tato funkce získá od uživatele data z textového souboru."""
    print("Soubor umístěte do složky 'soubory', která leží v kořenovém \
          adresáři tohoto programu a zadejte název souboru, který chcete \
          načíst.")
    nazevSouboru = input("Předpokládá se kódování utf-8. \n\n\t\t:")

    # Získat cestu k složce "soubory" ve stejné složce jako zdrojový kód
    cestaSlozka = os.path.join(os.path.dirname(__file__), "soubory")

    # Kontrola, jestli existuje složka 'soubory'
    if not os.path.exists(cestaSlozka):
        raise FileNotFoundError("Složka 'Soubory' neexistuje.")

    # Získat úplnou cestu k cílovému souboru
    cestaSoubor = os.path.join(cestaSlozka, nazevSouboru)

    # Zkontrolovat, zda soubor existuje
    if not os.path.exists(cestaSoubor):
        raise FileNotFoundError(f"Soubor {nazevSouboru} neexistuje.")
    # Načíst obsah souboru
    try:
        with open(cestaSoubor, 'r', encoding='utf-8') as file:
            obsah = file.read()
        return obsah
    except Exception as chyba:
        raise SystemError("Při načítání souboru došlo k chybě:", str(chyba))


def UlozSoubor(VystupniText):
    soubor = input("Vložte název souboru. Soubor bude uložen do složky \
                   'soubory' v kořenovém adresáři programu. POZOR - Pokud \
                   soubor již existuje, dojde k jeho přepsání \n\n\t")

    # Vytvoření cesty k souboru ve složce 'soubory'
    file_path = os.path.join("soubory", soubor)

    # Zkontroluje, zda složka neexistuje a pokud ne, tak ji hned vyrobíme.
    if not os.path.exists("soubory"):
        os.makedirs("soubory")

    # Otevření souboru s kódováním UTF-8 a následný zápis.
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(VystupniText)


def Hra(VystupniText, VstupniText):
    print("Po stisku klávesy enter se zobrazí zpřeházený text a začne se \
          počítat čas. Začněte ihned číst text a po dočtení skitskněte opět \
          klávesu enter")
    getpass.getpass(prompt="")
    ZacatekA = time.time()
    cls()
    print(VystupniText)
    getpass.getpass(prompt="")
    KonecA = time.time()
    cls()
    CasA = KonecA - ZacatekA
    print(f"Hotovo, přelouskání zpřeházeného textu Vám trvalo {CasA:.2f} \
          sekund.\n Nyní stiskněte enter a ihned začněte číst text v \
          originálním znění. Po dočtení opět stiskněte klávesu enter. ")
    getpass.getpass(prompt="")
    cls()
    ZacatekB = time.time()
    print(VstupniText)
    getpass.getpass(prompt="")
    KonecB = time.time()
    cls()
    CasB = KonecB - ZacatekB
    if CasA > CasB:
        print(f"Přečtení originálního textu Vám trvalo {CasB:.2f} sekund.\nTo \
              je o {(CasA - CasB):.2f} sekund rychleji.")
    elif CasA < CasB:
        print(f"Rozházený text jste přečetli o {(CasB - CasA):.2f} sekund \
              rychleji, než originál!\n Buď jste génius nebo šílenec!!!")
    else:
        print("Časy jsou shodné!!!")

    print("\n\n\t Stiskněte enter pro ukončení")
    getpass.getpass(prompt="")
    sys.exit()

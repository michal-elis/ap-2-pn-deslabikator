"""Hlavní soubor programu Deslabikátor.
obsahuje funkce menu, které se použijí pro interakci s uživatelem"""
import funkce
import menu
import sys
import click
import getpass


def FunkceMenu2(VystupniText, VstupniText):
    """Funkce druhého menu, které se použije po načtení dat."""
    funkce.cls()
    print(menu.Menu2)
    while True:
        volba = click.getchar()
        if volba == '1':
            funkce.cls()
            print(VystupniText)
            print("\n\n\t Stiskněte enter pro ukončení")
            getpass.getpass(prompt="")
            sys.exit()
        elif volba == '2':
            funkce.cls()
            funkce.UlozSoubor(VystupniText)
            print("Text byl úspěšně uložen do souboru \n\n \
                  Stiskněte enter pro ukončení programu")
            getpass.getpass(prompt="")
            sys.exit()
        elif volba == '3':
            funkce.cls()
            funkce.Hra(VystupniText, VstupniText)
        elif volba == '4':
            funkce.cls()
            print("Nashledanou\n")
            sys.exit()


def FunkceMainMenu():
    """Funkce hlavního menu s výběrem čísla volby pomocí modulu click."""
    print(menu.MainMenu)
    while True:
        volba = click.getchar()
        if volba == '1':
            funkce.cls()
            VstupniText = input("Vložte vstupní text: \n \n \t \t")
            FunkceMenu2(funkce.deslabikace(VstupniText), VstupniText)
        elif volba == '2':
            funkce.cls()
            VstupniText = funkce.NactiSoubor()
            FunkceMenu2(funkce.deslabikace(VstupniText), VstupniText)
        elif volba == '3':
            funkce.cls()
            print(menu.Info, "\n\n")
            print(menu.MainMenu)
        elif volba == '4':
            funkce.cls()
            print("Nashledanou\n")
            sys.exit()


if __name__ == "__main__":
    funkce.cls()
    print(menu.Spusteni)
    FunkceMainMenu()

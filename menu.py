""" 
menu.py 
Aby byl hlavní soubor programu čitelnější, jsou texty pro výpis jednotlivých menu umístěny zde.
"""
import textwrap, os, sys, funkce
def cls():
    """
       Funkce pro vyčištění textu na obrazovce
    """
    if os.name == "nt":
        prikaz = "cls" # Windows
    else:
        prikaz = "clear" # Linux

    os.system(prikaz) 




   
Spusteni = textwrap.fill("Výtejte v programu Deslabikátor. Tento program má za úkol demonstrovat, že lidský mozek nečte slova \
po jednotlivých písmenech, ale jako množinu znaků, které nemusí být ve správném pořadí. Stačí aby bylo na správném místě první \
a poslední písmeno. Zbytek může být rozmístěn náhodně a lidský mozek dokáže i tak text téměř bez problémů přečíst. \n \n ", 120) # Text se vypíše se správným zalomením

MainMenu = """
    ╔════════════════════════════════════════════════════════════════╗
    ║ *  MENU - pro výběr stisknětě číslo odpovídající Vaší volbě  * ║
    ╠════════════════════════════════════════════════════════════════╣
    ║ 1.   Vložte vstupní text psaním na klávesnici                  ║
    ║ 2.   Vložte vstupní text ze souboru                            ║
    ║ 3.   Info                                                      ║
    ║ 4.   KONEC                                                     ║
    ╚════════════════════════════════════════════════════════════════╝
"""

Menu2 = """
Vaše data byla načtena v pořádku.

    ╔════════════════════════════════════════════════════════════════╗
    ║ *  MENU - pro výběr stisknětě číslo odpovídající Vaší volbě  * ║
    ╠════════════════════════════════════════════════════════════════╣
    ║ 1.   Zobrazit zpřeházený text na obrazovce                     ║
    ║ 2.   Uložit zpřeházený text do souboru                         ║
    ║ 3.   Minihra - čtení na čas                                    ║
    ║ 4.   KONEC                                                     ║
    ╚════════════════════════════════════════════════════════════════╝
"""

NactiZeSouboru = "Soubor umístěte do složky 'soubory', která leží v kořenovém adresíři tohoto programu a zadejte název souboru, který chcete načíst."
#cls()
#print(Spusteni)
#FunkceMainMenu()
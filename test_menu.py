"""Testovací soubor menu.

Menu není jak testovat, protože neobsahuje funkce ani žádný spustitelný \
kód, ale pouze texty, které se vypisují v menu programu. Nicméně smazáním \
tohoto souboru přijdu o 5% coverage, takže ho tu nechávám :-(
"""
import menu


def test_NactiZeSouboru():
    """Nesmyslný test, který kontroluje pouze to, že v proměnné je to,
    co tam má být.
    """
    assert menu.NactiZeSouboru == "Soubor umístěte do složky 'soubory', která \
leží v kořenovém adresíři tohoto programu a zadejte název souboru, který \
chcete načíst."

# Závěrečný projekt z předmětu AP2PN
Tento repozitář slouží jako podklad a vzor pro závěrečný projekt z předmětu AP2PN.

## Požadavky na projekt
* Projekt musí být napsán v programovacím jazyce Python 3.
* Témata projektu jste si volili dříve na Moodle.
* Kód musí být okomentovaný/dokumentovaný (ideálně všechny entity).
* Kód musí obsahovat unit testy (pokrytí kódu testy by se mělo blížit 100%, testy ověřují jak validní tak chybné použití funkcí).
* Zdrojový kód musí projít kontrolním testem na gitlabu definované v gitlab-cli.yml na vzorovém [repozitáři](https://git.fai.utb.cz/tureckova/ap2pn-projekt):
    * Musí projít všechny testy pomocí knihovny pdoc s pokrytím kódu minimálně 66%.
    * Kontola pomocí flake8 a flake8-docstrings nevrací žádné chyby.
    * Automaticky se vygeneruje dokumentace z docstringů pomocí knihovny pdoc.


## Postup
1. Přihlaste se na školní instanci [GitLab](https://git.fai.utb.cz/), přihlašovaní údaje jsou stejné jako do Stag či Moodle.

1. Nastavte si přístup na GitHub z vašeho počítače pomocí SSH klíče, [návod](https://moodle.utb.cz/mod/page/view.php?id=654046) je k dispozici na Moodle.

1. Proveďte Fork tohoto repozitáře: použijte tlačítko Fork na https://git.fai.utb.cz/tureckova/ap2pn-projekt.
        
1. Naklonujte si svůj repozitář a nastavte si upstream:

    Naklonování vašeho repozitáře do aktuálního adresáře:
    
        git clone git@git.fai.utb.cz:our-username/ap2pn-projekt.git
        
    Přejděte do adresáře s naklonovaným repozitářem:
    
        cd ap2pn-projekt
        
    Přiřaďte originální repozitář k vašemu forku:
    
        git remote add upstream https://git.fai.utb.cz/tureckova/ap2pn-projekt/

    Stáhněte si aktualizace z originálního repozitáře, přijetí změn z upstream:

        git pull upstream main
    
1. Spusťte defaultní pipeline Pipelines > Run Pipelines. Vzorový projekt by měl projít bez chyb (Passed) všechny fáze Pipeline (Build > Pipelines). Pod tlačítkem *dowload* vpravo na řádku je možné stáhnout **Artifacts** a prohlédnout si vygenerovanou dokumentaci.
    
1. Commitujte vaše změny po logických oddílech, každý commit s výstižným popisem:

        git commit -m "logical commit description"
    
1. Proveďte push vašich změn na server a zkontolujte, že prochází (Passed) všechny fáze Pipeline (Build > Pipelines):

        git push
    
1. Přizvěte vyučující tureckova@utb.cz k úpravám projektu: Manage > Members > Invite members, zvolte roli Developer.  
Do moodlu odejte odkaz na gitlab stránku vašeho projektu - url adresu forku vašeho projektu.

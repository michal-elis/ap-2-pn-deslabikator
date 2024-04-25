# Dokumentace k programu DESLABIKÁTOR   

## Úvod

Tento program vznikl v dubnu 2024 jako semestrální práce Michala Elise do předmětu 'Pokročilé nástroje pro vývoj' na FAI Univerzity Tomáše Bati a má za úkol demonstrovat, že lidský mozek nečte slova 
po jednotlivých písmenech, ale jako množinu znaků, které nemusí být ve správném pořadí. Stačí aby bylo na správném místě první a poslední písmeno. Zbytek může být rozmístěn náhodně a lidský mozek dokáže i tak text téměř bez problémů přečíst.\
Průměrný časový rozdíl na Anglicky psaném textu u rodilého mluvčího je pouhých 11%



**Někdy začátkem roku 2003 jste mohli na internetu nebo v novinách zahlédnout následující zprávu:**
>*Při vzýkmuu na Uinvreztiě v Cmabrigdi zijsitli, že k tmou, aby byl čolěvk sochepn peřčíst psnaý txet, nmesuí být znkay ve solevch zapasné ve srpávénm přodaí. Stčaí, kydž josu na sývch msíetch jen pvrní a psolendí psínema. Lisdký mzoek tak je sochepn bez věštích prbloémů čsít i txet, ketrý zdnálviě ndáevá smsyl.*

To, že se jedná o zjištění vědců z univerzity Cambridge není pravda. Univerzita se tímto tématem nikdy nezabývala. Ve skutečnosti si tohoto fenoménu poprvé všimnul Graham Rawlinson, který jej zdokumentoval v roce 1976 ve své [disertační práci](https://www.mrc-cbu.cam.ac.uk/people/matt.davis/Cmabrigde/rawlinson/) na univerzite Nottingham.

Velmi dobrý článek (anglicky), který popisuje, jak tato fáma vznikla si můžete přečíst na stránkách univezity [zde](https://www.mrc-cbu.cam.ac.uk/people/matt.davis/cmabridge/)


## Instalace

Pro nainstalování programu Deslovníkátor budete potřebovat Git a Python. Pokud je již máte, můžete některé následující kroty přeskočit.  



1. **Stažení Gitu:**
   
    Stáhněte a nainstalujte si Git z oficiálních stránek https://git-scm.com/  

1. **Stažení Pythonu:**
    
    Stáhněte a a nainstalujte si Python: https://www.python.org/downloads/
1. **Stažení repozitáře:**
    
    Spusťje si příkazovou řádku, najeďte si do umístění, kam budete chtít program instalovat a spusťte následující kód:
    ```bash
    git clone https://git.fai.utb.cz/m_elis/ap-2-pn-deslabikator.git
    ```

1. **Instalace potřebných souborů:**
    Pro doinstalování potřebných modulů spusťte následující kód:
    ```bash
    py -m pip install -r requirements.txt
    ```


1. **Spuštění aplikace:**
    
    Aplikaci spustíte pomocí dávkového souboru deslovnikator.bat v kořenové složce aplikace


## Použití aplikace

Po spuštění aplikace se objeví jednduché menu, s popisem jednotlivých voleb. Můžete načíst text z textového souboru kódovaného v utf-8 nebo zadat text psaním na klávesnici. Po načtení textu si můžete jeho upravenou verzi zobrazit na monitoru, uložit do souboru nebo si můžete zkusit zahrát minihru a otestovat své schopnosti na čas.



## Licence

Jedná se o open source projekt pod [licencí MIT](MIT.md).

## Přejeme Vám příjemnou zábavu při používání programu

<br />

<div style="text-align:center">

![Pá](pa.gif)

</div>



[^1]: Poznámka
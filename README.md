# Projekts
## Kriptovalūtas cenas un tās izmaiņu izsekošana

### Programmatūras mērķis 
Šī programmatūra ir izstrādāta, lai izsekotu vajadzīgo kriptovolūtu cenām. Cenu izsekošanai izmanto kriptovalūtu biržu Binance.com (http://www.binance.com/). Es paņēmu kriptovalūtas, kas man bija vajadzīgas: bitcoin, ethereum un solana, ko var aizstāt, mainot to kārtas numuru, kas atbilst Binance.com sadaļā "Markets" (https://www.binance.com/en/markets/overview) norādītajam. Programma nodrošina šo kriptovalūtu pašreizējo cenu un procentuālās izmaiņas pēdējo 24 stundu laikā.

Papildus jau iepriekš uzdoto kriptovalūtu izsekošanai programma sniedz informāciju arī par pieciem ievērojamākajiem cenu kritumiem pēdējo 24 stundu laikā, kā arī pieciem pieauguma līderiem, kas dod iespēju operatīvi veikt kādas izmaiņas.
Tāpat programma arī ļauj papildus ievadīt jebkuras kriptovalūtas nosaukumu un iegūt informāciju par uzdoto kriptovalūtu. Programma automātiski izgūst datus par norādīto kriptovalūtu, arī uzrādot cenu un izmaiņas pēdējo 24 stundu laikā.

Tā kā es aktīvi interesējos par kriptovalūtas tirgu un man ir daži aktīvi, šī programma ļaus man nedaudz atvieglot tirgus monitoringu.

### Izmantoto Python bibliotēku apraksts

Lai šī programmatūra darbotos, tiek izmantotas vairākas Python bibliotēkas: `selenium`,`time`,`termcolor`.

#### Selenium bibliotēka
`Selenium WebDrive` - pārlūkprogrammas pārvaldības bibliotēka. Tā ļauj mijiedarboties ar tīmekļa lapām un veikt dažādas darbības.

Šajā gadījumā bibliotēka tiek izmantota, lai palaistu Chrome tīmekļa pārlūkprogrammu un mainītu tās konfigurāciju (mainīt pārlūkprogrammas loga lielumu - **driver.set_window_size(1920,1080)**), šim nolūkam tiek izmantots `Webdriver`. Pārlūkprogrammas loga maiņa ir nepieciešama, jo nepilnā logā Binance vietnes interfeiss mainās un kods nevarēs korekti darboties.

`Selenium` - bibliotēka, lai automatizētu pārlūkprogrammas darbības. Tā ļauj programmatiski sadarboties ar tīmekļa lapām, veikt dažādas darbības, kā arī iegūt dažādu informāciju no tīmekļa lapām.

Šajā gadījumā `Selenium` bibliotēka tiek izmantota, lai atvērtu Binance.com tīmekļa lapu, meklētu dažādus elementus, mijiedarbotos ar tiem un izgūtu datus.

#### Time bibliotēka
`Time` - iebūvēta bibliotēka, kas ļauj strādāt ar laiku. Tā tiek izmantota, lai pievienotu laika aizkavi **time.sleep()**, piemēram, lai nodrošinātu tīmekļa lapas pilnīgu ielādi. Šajā kodā šī bibliotēka tiek izmantota tieši šādiem mērķiem, lai sinhronizētu ar tīmekļa lapas lejupielādi.

#### Termcolor bibliotēka
`Termcolor` - bibliotēka ļauj konsolei izvadīt krāsainu tekstu. Tas uzlabo izvades lasāmību, padarot to izteiksmīgāku. Šajā programmā dažas daļas konsolē tiek attēlotas dažādās krāsās, kas uzlabo vizuālo uztveri.

### Programmatūras izmantošanas metodes
1. Pēc programmas palaišanas atveras tīmekļa pārlūkprogramma ar Binance vietni, tiek veikta 1 sekundes aizkave, izmantojot komandu **time.sleep()** un tiek apstiprināta cookie failu izmantošana, un pārslēdzas uz sadaļu "Markets". 
2. Sadaļa "Markets" tiek parādīta informācija par galvenajām kriptovalūtām, kas pēc noklusējuma ir sakārtotas pēc tirgus apjoma, no šīs lapas tiek izgūta informācija par to cenu un procentu izmaiņām pēdējo 24 stundu laikā, izmantojot metodi **driver.find_element(By.CSS_SELECTOR, ...)**.
3. Pēc pirmās darbības tīmekļa lapā sākas nākamais for cikls, tiek atrasts elements, kas atbilst "Сhange" pogai, pēc kura tas tiek nospiest un un dati tiek izgūti, šī darbība notiek divas reizes.
4. Pēc tam var ievadīt konkrētas kriptovalūtas nosaukumu, lai iegūtu detalizētu informāciju par šo valūtu.

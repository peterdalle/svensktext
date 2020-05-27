# Svensk text

**Svensk text** är en samling med data för språkresurser på svenska speciellt anpassat för att snabbt kunna läsas in av programspråk som Python, R eller dylikt.

Syftet är att samla svenska resurser som:

- är fria att använda
- finns i flera öppna standardiserade format som CSV och JSON
- har en enkel datastruktur
- kan enkelt maskinläsas
- består av små filer utan onödigt krimskrams
- har exempelkod i R och Python för snabb användning

## Alla resurser

Kategori         | Resurs                                | Antal   | Beskrivning
:--------------- | :------------------------------------ | ------: | :-------------------------------------------- 
Namn             | [Förnamn](namn/)                      | 25166   | Namn på män och kvinnor
Namn             | [Efternamn](namn/)                    | 1000    | Vanliga efternamn i Sverige
Nationaliteter   | [Nationaliteter](nationaliteter/)     | 197     | Nationaliteter med namn på invånarna i landet, både singular och plural
Platser          | [Svenska orter](platser/)             | 2007    | Namn på svenska orter
Platser          | [Sveriges län](platser/)              | 21      | Sveriges län
Platser          | [Sveriges kommuner](platser/)         | 290     | Sveriges kommuner
Platser          | [Länder och huvudstäder](platser/)    | 200     | Världens länder samt deras huvudstäder
Platser          | [Landskoder](platser/)                | 245     | Landskoder (ISO 3166-1)
Platser          | [Valutor](platser/)                   | 245     | Länder och deras valutor och valutakoder (ISO 4217)
Platser          | [Vägar](platser/)                     | 278     | Svenska Europavägar, riksvägar och landsvägar
Tider            | [Helgdagar](tider/)                   | 23      | Svenska helgdagar
Tider            | [Tidsperioder](tider/)                | 19      | Tidsenheter och tidsintervall
Tider            | [Månader](tider/)                     | 12      | Månader januari till december
Tider            | [Veckodagar](tider/)                  | 7       | Veckodagar måndag till söndag
Ord              | [Lemma](lemma/)                       | 675137  | Grundformen av ord (t ex "springa" är grundform av "sprungit" och "sprang")
Ord              | [Stoppord](stoppord/)                 | 437     | Svenska stoppord
Ord              | [Politiska stoppord](stoppord/)       | 285     | Svenska politiska stoppord
Ord              | [Sentimentlexikon](sentiment/)        | 2067    | Positiva och negativa svenska ord
Ord              | [Corona/smitta](lexikon/)             | 253     | Lexikon för ord relaterade till corona/smitta i nyhetsmedier
Jobb             | [Yrken](yrken/)                       | 13833   | Svenska yrkesbeteckningar inklusive om det är en manlig eller kvinnlig beteckning
Organisationer   | [Medier](organisationer/)             | 158     | Domäner till svenska massmedier och nyhetsmedier
Organisationer   | [Myndigheter](organisationer/)        | 354     | Namn på svenska myndigheter
Organisationer   | [EU-institutioner](organisationer/)   | 17      | Namn på EU:s institutioner och organ
Wikipedia        | [Wikipedia-titlar](wikipedia/)        | 6130751 | Alla titlar på svenska Wikipedia-sidor

## Vill du hjälpa till?

[Läs hur du  kan bidra](CONTRIBUTE.md) till Svensk text.

I korthet: bidra med komma-separerade CSV-filer (som har en header på engelska) och som får användas fritt.

## Se även

- [Språkbankens resurser på Göteborgs universitet](https://spraakbanken.gu.se/swe/resurser)
- [Öppna data](https://oppnadata.se/)
- [Statistiska centralbyrån](http://www.scb.se/)
- [Bebyggelseregistret – BeBR](https://www.raa.se/hitta-information/bebyggelseregistret-bebr/)
- [Lantmäteriet](https://www.lantmateriet.se/) ([öppna geodata](https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/oppna-data/))
- [Öppna data från SKL](https://skl.se/naringslivarbetedigitalisering/digitalisering/informationsforsorjningochdigitalinfrastruktur/oppnadata/sklsoppnadata.psidata.html)
- [Valmyndigheten](https://www.val.se/)
- [Rikstermbanken](http://www.rikstermbanken.se/)

## Citera

Svensk text finns på [Svensk nationell datatjänst](https://snd.gu.se/sv/catalogue/study/ext0278) och kan citeras på följande sätt:

> Dahlgren, P. M. (2018). Svensk text. *Svensk nationell datatjänst*. https://snd.gu.se/sv/catalogue/study/ext0278

BibTeX:

```
@misc{dahlgren_svensktext_2018,
	title = {Svensk text},
	url = {https://snd.gu.se/sv/catalogue/study/ext0278},
	abstract = {Samling med språkresurser på svenska speciellt anpassat för att snabbt och enkelt kunna läsas in av programspråk som Python, R eller dylikt. Bland språkresurserna finns namn på kvinnor (förnamn), män (förnamn), städer, kommuner, län, huvudstäder, länder, nationaliteter, yrken, myndigheter, massmedier med mera. Syftet är att samla svenska resurser som är fria att använda, finns i flera öppna standardiserade format (exempelvis CSV och JSON), har en enkel datastruktur som enkelt kan maskinläsas, består av små filer utan onödigt krimskrams och har exempelkod (R och Python) för att snabbt kunna användas. Materialet utökas och uppdateras kontinuerligt under öppna licenser.},
	language = {Svenska},
	urldate = {2018-12-20},
	publisher = {Svensk nationell datatjänst},
	author = {Dahlgren, Peter M.},
	month = dec,
	year = {2018},
	note = {https://github.com/peterdalle/svensktext}
}
```
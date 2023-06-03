# Svensk text

**Svensk text** är en samling med data för språkresurser på svenska speciellt anpassat för att snabbt kunna läsas in av vanliga programspråk.

Syftet är att samla svenska resurser som:

- är fria att använda
- finns i flera öppna standardiserade format som CSV och JSON
- har en enkel datastruktur
- kan enkelt maskinläsas
- består av små filer utan onödigt krimskrams
- kan läsas in i [bibliotek för R](https://github.com/peterdalle/svensktext-rpackage), Python och C#

## Alla resurser

Kategori         | Resurs                                | Antal   | Beskrivning
:--------------- | :------------------------------------ | ------: | :-------------------------------------------- 
Namn             | [Tilltalsnamn](namn/)                 | 103584  | Tilltalsnamn på män och kvinnor i Sverige
Namn             | [Förnamn](namn/)                      | 163213  | Förnamn på män och kvinnor i Sverige
Namn             | [Efternamn](namn/)                    | 382492  | Efternamn i Sverige
Nationaliteter   | [Nationaliteter](nationaliteter/)     | 197     | Nationaliteter med namn på invånarna i landet, både singular och plural
Platser          | [Svenska orter](platser/)             | 2007    | Namn på svenska orter
Platser          | [Sveriges län](platser/)              | 21      | Sveriges län
Platser          | [Sveriges kommuner](platser/)         | 290     | Sveriges kommuner
Platser          | [Länder och huvudstäder](platser/)    | 202     | Världens länder samt deras huvudstäder
Platser          | [Landskoder](platser/)                | 245     | Landskoder (ISO 3166-1)
Platser          | [Valutor](platser/)                   | 245     | Länder och deras valutor och valutakoder (ISO 4217)
Platser          | [Vägar](platser/)                     | 278     | Svenska Europavägar, riksvägar och landsvägar
Tider            | [Helgdagar](tider/)                   | 23      | Svenska helgdagar
Tider            | [Tidsperioder](tider/)                | 27      | Tidsenheter och tidsintervall
Tider            | [Månader](tider/)                     | 12      | Månader januari till december
Tider            | [Veckodagar](tider/)                  | 7       | Veckodagar måndag till söndag
Ord              | [Lemma](lemma/)                       | 675137  | Grundformen av ord (t ex "springa" är grundform av "sprungit" och "sprang")
Ord              | [Stoppord](stoppord/)                 | 438     | Svenska stoppord
Ord              | [Politiska stoppord](stoppord/)       | 285     | Svenska politiska stoppord
Ord              | [Sentimentlexikon](sentiment/)        | 2067    | Positiva och negativa svenska ord
Ord              | [Emotioner](emotioner/)               | 8519    | Känsloladdade ord och deras intensitet, uppdelade på 8 känslor
Ord              | [Moral](moral/)                       | 2104    | Moraliska ord enligt Moral Foundations Theory, uppdelade på 5 fundament
Ord              | [Corona/smitta](lexikon/)             | 594     | Lexikon för ord relaterade till corona/smitta i nyhetsmedier
Jobb             | [Yrken](yrken/)                       | 13833   | Svenska yrkesbeteckningar inklusive om det är en manlig eller kvinnlig beteckning
Organisationer   | [Medier](organisationer/)             | 158     | Domäner till svenska massmedier och nyhetsmedier
Organisationer   | [Myndigheter](organisationer/)        | 354     | Namn på svenska myndigheter
Organisationer   | [EU-institutioner](organisationer/)   | 17      | Namn på EU:s institutioner och organ
Wikipedia        | [Wikipedia-titlar](wikipedia/)        | 6130751 | Alla titlar på svenska Wikipedia-sidor

## Programbibliotek

- [svensktext för R](https://github.com/peterdalle/svensktext-rpackage)
- svensktext för Python ([läs mer](src/))
- svensktext för C# ([läs mer](src/))

## Vill du hjälpa till?

Läs mer om hur du kan [bidra med CSV-filer](CONTRIBUTE.md) med öppen data.

## Vill du använda datan? Gör en kopia.

Gör helst en egen lokal kopia. Både datan och strukturen kan nämligen ändras varefter som den utökas.

## Citera

Svensk text finns på [Svensk nationell datatjänst](https://snd.gu.se/sv/catalogue/study/ext0278) och kan citeras på följande sätt:

APA6:

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

## Publikationer som använder datan

- Rivera Ahlin, K. (2023). [*Fixation and Machine Learning: A new method for measuring fixation in internet users using machine learning and natural language processing*](https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1751467&dswid=9795). Uppsala: Institutionen för informationsteknologi, Uppsala universitet.
- Dahlgren, P. M. (2021). Svenskar eller utrikesfödda i medierna? – att identifiera födelseland från namn. I: L. Truedson & J. Lundqvist (Red.), [*Vitt eller brett? - vilka får ta plats i medier och på redaktioner?*](https://mediestudier.se/publikationer/vitt-eller-brett/) (s. 79–91). Stockholm: Institutet för mediestudier.
- Dahlgren, P. M. (2021). [*Medieinnehåll och mediekonsumtion under coronapandemin: Datoriserade metoder för insamling och analys av stora mängder text- och mediedata (arbetsrapport nr 88)*](https://www.gu.se/jmg/var-forskning/publikationer/jmgs-rapportserie). Göteborg: Institutionen för journalistik, medier och kommunikation (JMG), Göteborgs universitet.
- Chen Trieu, K. & Nguyen, L. (2020). [*Classifying Short Clinical Notes: An Unsupervised Approach*](https://odr.chalmers.se/items/de8a8de5-b494-43da-8cb7-fe12d2a4f117). Göteborg: Institutionen för data och informationsteknik, Chalmers tekniska högskola.

Säg gärna till så lägger jag till din publikation här (eller gör det själv genom en [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)).

## Se även

- [Språkbankens resurser på Göteborgs universitet](https://spraakbanken.gu.se/swe/resurser)
  - [Förtränade inbäddningar - En lista över förtränade inbäddningar för svenska](https://spraakbanken.gu.se/resurser/embeddings)
- [Öppna data](https://oppnadata.se/)
- [Statistiska centralbyrån](http://www.scb.se/)
- [Bebyggelseregistret – BeBR](https://www.raa.se/hitta-information/bebyggelseregistret-bebr/)
- [Lantmäteriet](https://www.lantmateriet.se/) ([öppna geodata](https://www.lantmateriet.se/sv/Kartor-och-geografisk-information/oppna-data/))
- [Öppna data från SKL](https://skl.se/naringslivarbetedigitalisering/digitalisering/informationsforsorjningochdigitalinfrastruktur/oppnadata/sklsoppnadata.psidata.html)
- [Valmyndigheten](https://www.val.se/)
- [Rikstermbanken](http://www.rikstermbanken.se/)
- [PAP API Lite - öppet REST API med Sveriges postnummer och postorter](https://papilite.se/)
- [Dataportal](https://www.dataportal.se/) - sök och utforska öppna data i Sverige (från Myndigheten för digital förvaltning, DIGG)

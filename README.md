# Svensk text

Samling med språkresurser på svenska: kvinno- och mansnamn, ortsnamn, länsnamn, landsnamn, nationaliteter, yrken, sentimentlexikon samt stoppord.

Syftet är att samla svenska resurser som:

- är fria att använda
- finns i flera öppna standardiserade format som CSV och JSON
- har en enkel datastruktur
- kan enkelt maskinläsas
- består av små filer utan onödigt krimskrams

Katalogen [/src](/src) innehåller kod för att konvertera originalfilerna till och från JSON respektive CSV.

Vill du hjälpa till? [Läs hur du kan bidra](CONTRIBUTE.md).

## Namn

25 166 namn på kvinnor och män ([CSV](namn/namn.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`name` | Personnamnet  | Text
`gender` | Om det är ett kvinnonamn (`female`) eller mansnamn (`male`) | Text

Finns även som separata filer:

- 13 411 kvinnonamn ([JSON](namn/kvinnonamn.json), [CSV](namn/kvinnonamn.csv))
- 11 755 mansnamn ([JSON](namn/mansnamn.json), [CSV](namn/mansnamn.csv))

<!--
```py
# Importera i Python med pandas.
import pandas as pd
df_kvinnonamn = pd.read_json("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/kvinnonamn.json")
df_mansnamn = pd.read_json("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/mansnamn.json")
df_namn = pd.read_csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/namn.csv", sep=",", header=2)```

```py
# Importera i R.
df_kvinnonamn = read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/kvinnonamn.csv", sep=";")df_mansnamn = read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/mansnamn.csv", sep=";")
df_namn = read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/namn.csv", sep=";")```
-->

Källa: [Mattias Hising](https://github.com/hising/svensk-data)

## Nationaliteter

197 nationaliteter med namn på invånarna i landet, både singular och plural ([JSON](nationaliteter/nationaliteter.json), [CSV](nationaliteter/nationaliteter.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`id` | Godtyckligt ID på landet (från 0 till 196)  | Heltal
`country` | Namnet på landet (t.ex. Storbritannien) | Text
`country_alternativename` | Alternativt namn på landet | Text
`resident_singular` | Vad invånarna kallas i singular (t.ex. britt) | ['Lista']
`resident_plural` | Vad invånarna kallas i plural (t.ex. britter) | ['Lista']
`adjective` | Vad invånarna kallas som adjektiv (t.ex. brittisk) | Text

Källa: [TT-språket](https://tt.se/tt-spraket/ord-och-begrepp/internationellt/stat-och-nationalitet/)

## Svenska orter

2 007 namn på svenska orter ([JSON](platser/ortsnamn.json)).

Källa: [Mattias Hising](https://github.com/hising/svensk-data)

## Sveriges län

Sveriges 21 län ([CSV](platser/lan.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`name` | Namnet på länet | Text
`letter` | Länsbokstav | Text
`code` | Länskod | Text
`area` | Yta | Heltal
`population` | Folkmängd (2018-03-31) | Heltal
`population_per_square_km` | Invånare per kvadratkilometer | Decimaltal
`residencetown` | Residensstad | Text
`municipalities` | Antal kommuner i länet | Heltal
`founded ` | Året då länet inrättades | Text
`order_from_north_to_south` | Ordningen från norr till söder (residensstad) | Heltal

Källa: [Wikipedia - Sveriges län](https://sv.wikipedia.org/wiki/Sveriges_l%C3%A4n#Lista_%C3%B6ver_Sveriges_l%C3%A4n)

## Sveriges kommuner

Sveriges 290 kommuner ([CSV](platser/kommuner.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
code | Kommunkod | Tal
name | Kommunens namn | Text
region | Län | Text
population | Folkmängd | Decimaltal
area | Total areal, kvadratkilometer | Decimaltal
land | Landareal, kvadratkilometer | Decimaltal
sea | Inlandsvattenareal, exklusive fyra största sjöarna, kvadratkilometer | Decimaltal
ocean | Havsvattenareal, kvadratkilometer | Decimaltal
density | Befolkningstäthet, invånare per kvadratkilometer land | Decimaltal
bounds_ne_lat_google_2015_05_28 |  | Decimaltal
bounds_ne_lng_google_2015_05_28 |  | Decimaltal
bounds_sw_lat_google_2015_05_28 |  | Decimaltal
bounds_sw_lng_google_2015_05_28 |  | Decimaltal
location_lat_google_2015_05_28 |  | Decimaltal
location_lng_google_2015_05_28 |  | Decimaltal

(Data städad genom att göra om header till engelska namn samt ta bort mellanslag som tusentalavgränsare.)

Källa: [Marcus Asplund](https://github.com/marcusasplund/kommundata)

## Länder och huvudstäder

Världens 199 länder samt deras huvudstäder ([CSV](platser/lander.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
 `country` | Namnet på landet | Text
 `capital` | Namnet på huvudstaden | Text

Källa: [Världens flaggor](http://www.flaggorvarlden.se/lista)

## Landskoder

245 landskoder i ISO 3166-1-format ([CSV](platser/landskoder.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`code2` | Landskod i versaler om 2 bokstäver | Text
`code3` | Landskod i versaler om 3 bokstäver | Text
`number` | Nummer på land om 3 siffror | Tal
`country` | Namnet på landet | Text

Källa: [ISO 3166-1-koder](https://sv.wikipedia.org/wiki/ISO_3166)

## Stoppord

427 svenska stoppord ([CSV](stoppord/stoppord.csv)).

285 svenska politiska stoppord ([CSV](stoppord/stoppord-politik.csv)). Framför allt baserad på stoppordlistan ovan.

Källa: [Nico Lehmann](https://github.com/ekorn/Keywords/tree/master/stopwords), kompletterad av Peter Dahlgren

## Sentimentlexikon

2 067 svenska ord med sentiment ([CSV](sentiment/sentimentlex.csv)). Fördelningen är ungefär 700 negativa ord och 1 300 positiva ord.

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`word` | |
`polarity` | |
`strength` | |
`sense` | |
`written_form` | |
`part_of_speech` | |
`confidence` | |
`lemgram` | |
`lemgram_frequency` | |
`lemma_frequency` | |
`example` | |

Källa: [Sentimentlexikon från Språkbanken](<https://spraakbanken.gu.se/swe/resurs/sentimentlex>) är licensierad med CC-BY (attribution). Använd följande artikel som referens för lexikonet: *Nusko, Bianka and Tahmasebi, Nina and Mogren, Olof. 2016. Building a Sentiment Lexicon for Swedish*.

Det är svårt att hitta bra sentimentlexikon på svenska. Det finns några alternativ (dock med okänd licensform):

- https://github.com/michelleludovici/SynonymProject
- https://github.com/fnielsen/afinn

## Yrken

13 833 svenska yrkesbeteckningar inklusive om det är en manlig eller kvinnlig beteckning ([CSV](yrken/vocations.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`vocation` |  Namnet på yrket | Text
`gender` |  Om det är kvinnlig (`female`), manlig (`male`) eller okänd (`unknown`) yrkesbeteckning | Text

Källa: [Yrken från Språkbanken](<https://spraakbanken.gu.se/swe/resurs/vocation-list>) (`vocationTerms150120.utf.txt`) är licensierad med CC-BY (attribution).

## Medier

112 domäner till svenska nyhetsmedier ([CSV](medier/nyheter-domaner.csv)).

11 domäner till sidor om immigration, rasism, nazism och dylikt ([CSV](medier/immigration-domaner.csv)).

Källa: Bland annat mest delade länkar på #svpol.

## Myndigheter

Namn på svenska myndigheter. Textfiler exporterade direkt fårn SCB. *Att göra: gör om till CSV.*

Källa: [Myndighetsregistret SCB](http://www.myndighetsregistret.scb.se/)
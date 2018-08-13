# Svensk text

Samling med språkresurser på svenska: kvinno- och mansnamn, ortsnamn, länsnamn, stoppord, sentimentlexikon samt yrken.

Syftet är att samla svenska resurser som:

- är fria att använda
- finns i flera öppna standardiserade format som CSV och JSON
- har en enkel datastruktur
- består av små filer utan onödigt krimskrams

Katalogen [/src](/src) innehåller kod för att konvertera originalfilerna till och från JSON respektive CSV.

## Namn

- 13 411 namn på kvinnor ([JSON](namn/kvinnonamn.json), [CSV](namn/kvinnonamn.csv)).
- 11 755 namn på män ([JSON](namn/mansnamn.json), [CSV](namn/mansnamn.csv)).
- samt [CSV med alla namn](namn/namn.csv) med headers `name` och `gender` (`female` samt `male`).

Från: [Mattias Hising](https://github.com/hising/svensk-data)

## Platser: svenska orter

2 007 namn på svenska orter.

Från: [Mattias Hising](https://github.com/hising/svensk-data)

## Platser: Sveriges län

Sveriges 21 län.

CSV headers:

- `name` är namnet på länet
- `letter` är länsbokstaven
- `code` är länskoden
- `area` är ytan
- `population` är folkmängden (2018-03-31)
- `population_per_square_km` är invånare per kvadratkilometer
- `residencetown` är residensstad
- `municipalities` är antal kommuner i länet
- `founded ` är årdet då länet inrättades
- `order_from_north_to_south` är ordningen från norr till söder (residensstad)

Från: [Wikipedia - Sveriges län](https://sv.wikipedia.org/wiki/Sveriges_l%C3%A4n#Lista_%C3%B6ver_Sveriges_l%C3%A4n)

## Platser: länder och huvudstäder

Världens 199 länder samt deras huvudstäder ([CSV](platser/lander.csv)).

CSV headers:

- `country` är namnet på landet
- `capital` är landets huvudstad

Källa: [Världens flaggor](http://www.flaggorvarlden.se/lista)

## Stoppord

427 svenska stoppord, textfil med ett ord per rad.

Från: [Nico Lehmann](https://github.com/ekorn/Keywords/tree/master/stopwords), kompletterad av Peter Dahlgren

## Sentimentlexikon

2 067 svenska ord med sentiment, CSV-fil med ett ord per rad. Fördelningen är ungefär 700 negativa ord och 1 300 positiva ord.

CSV headers:

- `word`
- `polarity`
- `strength`
- `sense`
- `written_form`
- `part_of_speech`
- `confidence`
- `lemgram`
- `lemgram_frequency`
- `lemma_frequency`
- `example`

[Sentimentlexikon från Språkbanken](<https://spraakbanken.gu.se/swe/resurs/sentimentlex>) är licensierad med CC-BY (attribution). Använd följande artikel som referens för lexikonet: `Nusko, Bianka and Tahmasebi, Nina and Mogren, Olof. 2016. Building a Sentiment Lexicon for Swedish`

Det är svårt att hitta bra sentimentlexikon på svenska. Det finns några alternativ (dock med okänd licensform):

- https://github.com/michelleludovici/SynonymProject
- https://github.com/fnielsen/afinn

## Yrken

13 833 svenska yrkesbeteckningar inklusive om det är en manlig eller kvinnlig beteckning.

CSV headers:

- `vocation` är namnet på yrket
- `gender` anger om det är en manlig eller kvinnlig yrkesbeteckning (`male`, `female` eller `unknown`)

[Yrken från Språkbanken](<https://spraakbanken.gu.se/swe/resurs/vocation-list>) (`vocationTerms150120.utf.txt`) är licensierad med CC-BY (attribution).
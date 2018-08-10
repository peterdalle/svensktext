# Svensk text

Samling med språkresurser på svenska: kvinno- och mansnamn, ortsnamn, stoppord, sentimentlexikon samt yrken.

## Namn

13 411 namn på kvinnor samt 11 755 namn på män.

Från: Mattias Hising (https://github.com/hising/svensk-data)

## Platser: orter

2 007 namn på svenska orter.

Från: Mattias Hising (https://github.com/hising/svensk-data)

## Platser: län

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

Från: https://sv.wikipedia.org/wiki/Sveriges_l%C3%A4n#Lista_%C3%B6ver_Sveriges_l%C3%A4n

## Stoppord

427 svenska stoppord, textfil med ett ord per rad.

Från: Nico Lehmann (https://github.com/ekorn/Keywords/tree/master/stopwords), kompletterad med ord från Peter Dahlgren

## Sentimentlexikon

2 067 svenska ord med sentiment, CSV-fil med ett ord per rad.

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

Sentimentlexikon (<https://spraakbanken.gu.se/swe/resurs/sentimentlex>) från [Språkbanken](https://spraakbanken.gu.se/) är licensierad med CC-BY (attribution). Använd följande artikel som referens för lexikonet: `Nusko, Bianka and Tahmasebi, Nina and Mogren, Olof. 2016. Building a Sentiment Lexicon for Swedish`

## Yrken

13 833 svenska yrkesbeteckningar inklusive om det är ett manlig eller kvinnlig beteckning.

CSV headers:

- `vocation` är namnet på yrket
- `gender` anger om det är en manlig eller kvinnlig yrkesbeteckning (`male`, `female` eller `unknown`)

Yrken (`vocationTerms150120.utf.txt`) (<https://spraakbanken.gu.se/swe/resurs/vocation-list>) från [Språkbanken](https://spraakbanken.gu.se/) är licensierad med CC-BY (attribution).
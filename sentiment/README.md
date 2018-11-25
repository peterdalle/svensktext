# Sentimentlexikon

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
# Sentimentlexikon

## Filer

2 067 svenska ord med sentiment ([CSV](sentimentlex.csv)). Fördelningen är 735 negativa ord och 1 333 positiva ord.

## Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`word` | Ord | Text
`polarity` | Manuellt granskat om ordet är positivt (`pos`) eller negativt (`neg`) | Text
`strength` | Manuell granskad styrka på sentiment från `-4` till `4` (initialt -2/2) | Tal
`sense` | Semantisk mening (se [SALDO](https://spraakbanken.gu.se/resurs/saldo))| Text
`written_form` | | ['List']
`part_of_speech` | Adjektiv, adverb, verb etc. (`av`, `avh`, `avm`, `ava`, `vb`, `vbn`, `vba`, `ab`) | Text
`confidence` | Styrka från 0 till 1 på granskarnas säkerhet att `polarity` är korrekt | Decimaltal
`lemgram` | Grundform av ordet | Text
`lemgram_frequency` | Frekvens av lemgram i Gigaword korpus som stämmer överens med `sense` | Tal
`lemma_frequency` | Innehåller missing values kallat `None` | Tal 
`example` | Ett eller flera exempel på ordet i sammanhang | Text

## Källa

- [Sentimentlexikon från Språkbanken](<https://spraakbanken.gu.se/swe/resurs/sentimentlex>) är licensierad med CC-BY (attribution). Använd följande artikel som referens för lexikonet: *Nusko, Bianka and Tahmasebi, Nina and Mogren, Olof. 2016. Building a Sentiment Lexicon for Swedish*.

## Se även

- https://github.com/michelleludovici/SynonymProject
- https://github.com/fnielsen/afinn

## Källdkod

### Python

```py
# Import.
import pandas as pd

df = pd.read_csv("https://github.com/peterdalle/svensktext/raw/master/sentiment/sentimentlex.csv",
                na_values = "None",
                encoding = "utf-8",
                header = 0,
                sep = ",")

# Count number of negative and positive words.
df["polarity"].value_counts()
```

### R

```r
# Import.
df <- read.csv("https://github.com/peterdalle/svensktext/raw/master/sentiment/sentimentlex.csv", 
               na.strings = "None",
               encoding = "UTF-8",
               header = TRUE,
               sep = ",")

# Count number of negative and positive words.
table(df$polarity)
```
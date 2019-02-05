# Yrken

## Filer

13 833 svenska yrkesbeteckningar inklusive om det är en manlig eller kvinnlig beteckning ([CSV](vocations.csv)).

## Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`vocation` |  Namnet på yrket | Text
`gender` |  Om det är kvinnlig (`female`), manlig (`male`) eller okänd (`unknown`) yrkesbeteckning | Text

## Källa

- [Yrken från Språkbanken](<https://spraakbanken.gu.se/swe/resurs/vocation-list>) (`vocationTerms150120.utf.txt`) är licensierad med CC-BY (attribution).

## Källkod

### Python

```py
# Import.
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/yrken/vocations.csv",
                 header = 0)

# Distribution of female, male and unknown vocations.
df["gender"].value_counts()
```

### R

```r
# Import.
df <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/yrken/vocations.csv", 
         encoding = "UTF-8",
         header = TRUE)

# Distribution of female, male and unknown vocations.
table(df$gender)
```
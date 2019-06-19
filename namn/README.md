# Namn

## Filer

- 25 166 namn på kvinnor och män ([CSV](namn.csv))
- 13 411 enbart kvinnonamn ([JSON](kvinnonamn.json), [CSV](kvinnonamn.csv))
- 11 755 enbart mansnamn ([JSON](mansnamn.json), [CSV](mansnamn.csv))
- 1 000 efternamn ([CSV](efternamn.csv))

## Datastruktur

namn.csv:

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`name` | Personnamnet  | Text
`gender` | Om det är ett kvinnonamn (`female`) eller mansnamn (`male`) | Text

efternamn.csv:

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`lastname` | Personnamnet  | Text
`frequency` | Antal personer i Sverige som hade efternamnet 1994-1997 | Tal

## Källa

- Förnamn från [Mattias Hising](https://github.com/hising/svensk-data)
- Efternamn från [Språkbanken](https://spraakbanken.gu.se/lb/statistik/lbenamnalf.phtml)

## Källkod

### Python

```py
# Import.
import pandas as pd
df_kvinnonamn = pd.read_json("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/kvinnonamn.json")
df_mansnamn = pd.read_json("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/mansnamn.json")
df_namn = pd.read_csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/namn.csv", sep=",", header=0)
df_efternamn = pd.read_csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/efternamn.csv", sep=",", header=0)
```

### R

```r
# Import.
df_namn <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/namn.csv",
                    sep=",", encoding="UTF-8", stringsAsFactors=FALSE)
df_namn$gender <- as.factor(df_namn$gender)

df_kvinnonamn <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/kvinnonamn.csv",
                          sep=",", encoding="UTF-8", stringsAsFactors=FALSE, header=FALSE)
df_mansnamn <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/mansnamn.csv",
                        sep=",", encoding="UTF-8", stringsAsFactors=FALSE, header=FALSE)

df_efternamn <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/efternamn.csv",
                         sep=",", encoding="UTF-8", stringsAsFactors=FALSE)
```
# Namn

Alla förnamn och tilltalsnamn på kvinnor respektive män samt efternamn i Sverige. Totalt 649 289 namn.

Representerar den folkbokförda befolkningen med minst två bärare 31 december 2020.

## Filer

Fil | Beskrivning
:------- | :----------
[efternamn.csv](efternamn.csv) | 382 492 efternamn
[fornamn-kvinnor.csv](fornamn-kvinnor.csv) | 87 629 förnamn på kvinnor
[fornamn-man.csv](fornamn-man.csv) | 75 584 förnamn på män
[tilltalsnamn-kvinnor.csv](tilltalsnamn-kvinnor.csv) | 55 986 tilltalsnamn på kvinnor
[tilltalsnamn-man.csv](tilltalsnamn-man.csv) | 47 598 tilltalsnamn på män

## Datastruktur

Alla filer har samma struktur:

Kolumn | Beskrivning | Datatyp
:------- | :---------- | :----------
`name` | Namn | Text
`persons` | Antal personer i Sverige som hade namnet 31 december 2020 | Tal

## Källa

- [Befolkningsstatistik, SCB](https://www.scb.se/hitta-statistik/sverige-i-siffror/namnsok/)

## Källkod

### Python

```py
# Import.
import pandas as pd
url = "https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/tilltalsnamn-kvinnor.csv"
kvinnor = pd.read_csv(url, sep=",", header=0)
```

### R

```r
# Import.
url <- "https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/tilltalsnamn-kvinnor.csv"
kvinnor <- read.csv(url, sep=",", encoding="UTF-8", stringsAsFactors=FALSE)
```
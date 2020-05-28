# Stoppord

## Filer

- 438 svenska stoppord, som är väligt inkluderande för vad som räknas som stoppord där även värdeord finns med ([CSV](stoppord-mycket.csv)).
- 330 svenska stoppord, som endast innehåller de vanligaste småorden oberoende av typen av text ([CSV](stoppord.csv)). Använd denna om du är osäker på vilken du ska använda!
- 285 svenska politiska stoppord, som framför allt är lämplig för att användas inom politik ([CSV](stoppord-politik.csv)). Framför allt baserad på stoppord.csv.

## Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`word` | Stoppord | Text

## Källa

- [Nico Lehmann](https://github.com/ekorn/Keywords/tree/master/stopwords)
- Kompletterad av Peter Dahlgren

## Se även

- https://github.com/stopwords-iso/stopwords-sv/blob/master/stopwords-sv.txt
- https://github.com/codelucas/newspaper/blob/master/newspaper/resources/text/stopwords-sv.txt

## Källkod

### Python

```py
# Import stop words.
import pandas as pd
stopwords = pd.read_csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord.csv",
                         header = 1,
                         encoding = "utf-8")

# Print stop words.
stopwords["word"]
```

### R

```r
# Import stop words.
stopwords <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord.csv", 
                       header = TRUE, 
                       encoding = "UTF-8",
                       stringsAsFactors = FALSE)

# Print stop words.
stopwords$word
```

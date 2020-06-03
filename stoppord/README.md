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

def get_stopwords(wordlist = "standard"):
    if wordlist == "standard":
        url = "https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord.csv"
    elif wordlist == "many":
        url = "https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord-mycket.csv"
    elif wordlist == "politics":
        url = "https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord-politik.csv"
    else:
        raise ValueError("Argument 'wordlist' must be 'standard', 'many' or 'politics', not '{}'.".format(wordlist))
    return pd.read_csv(url, header=1, encoding="utf-8")

# Print stop words.
stopwords = get_stopwords()
stopwords["word"]
```

### R

```r
# Import stop words.
get_stopwords <- function(wordlist = "standard") {
  if (wordlist == "standard") {
    url <- "https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord.csv"
  } else if (wordlist == "many") {
    url <- "https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord-mycket.csv"
  } else if (wordlist == "politics") {
    url <- "https://raw.githubusercontent.com/peterdalle/svensktext/master/stoppord/stoppord-politik.csv"
  } else {
    stop(paste0("Argument 'wordlist' must be 'standard', 'many' or",
                " 'politics', not '", wordlist, "'."), call.=FALSE)
  }
  return(read.csv(url, header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE,
                  col.names=c("word")))
}

# Print stopwords.
stopwords <- get_stopwords()
stopwords$word
```

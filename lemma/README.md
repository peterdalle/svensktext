# Lemma

[Lemma](https://sv.wikipedia.org/wiki/Lemma) är grundformen av ett ord ("springa" är grundformen av "sprang" och "sprungit"), vilket är användbara i en [stemmer](https://sv.wikipedia.org/wiki/Stemmer).

## Filer

675 137 ordpar med lemma på svenska.

## Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`lemma` | Grundformen av ordet (t ex "springa") | Text
`word` | Varianter av ordet (t ex "sprungit") | Text

## Källa

- https://github.com/michmech/lemmatization-lists/, licensierad med Open Database License.

## Se även

- https://github.com/aaaton/golem
- http://snowball.tartarus.org/algorithms/swedish/stemmer.html

## Källkod

### Python

```py
# Import.
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/lemma/lemmatization.csv",
                encoding = "utf-8",
                header = 0,
                sep = ",")

# Count unique lemmas.
len(df["lemma"].unique())
```

### R

```r
# Import.
df <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/lemma/lemmatization.csv",
               header = TRUE,
               encoding = "UTF-8",
               stringsAsFactors = FALSE)

# Count unique lemmas.
NROW(unique(df$lemma))
```
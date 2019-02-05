# Stoppord

- 427 svenska stoppord ([CSV](stoppord.csv)).
- 285 svenska politiska stoppord ([CSV](stoppord-politik.csv)). Framför allt baserad på stoppordlistan ovan.

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`word` | Stoppord | Text

Källa: [Nico Lehmann](https://github.com/ekorn/Keywords/tree/master/stopwords), kompletterad av Peter Dahlgren

## Se även

- [stopwords-iso för svenska](https://github.com/stopwords-iso/stopwords-sv/blob/master/stopwords-sv.txt)

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

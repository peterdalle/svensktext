# Namn

## Filer

- 25 166 namn på både kvinnor och män ([CSV](namn.csv))
- 13 411 enbart kvinnonamn ([JSON](kvinnonamn.json), [CSV](kvinnonamn.csv))
- 11 755 enbart mansnamn ([JSON](mansnamn.json), [CSV](mansnamn.csv))

## Format

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`name` | Personnamnet  | Text
`gender` | Om det är ett kvinnonamn (`female`) eller mansnamn (`male`) | Text

Källa: [Mattias Hising](https://github.com/hising/svensk-data)

## Källkod

### Python

```py
# Import.
import pandas as pd
df_kvinnonamn = pd.read_json("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/kvinnonamn.json")
df_mansnamn = pd.read_json("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/mansnamn.json")
df_namn = pd.read_csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/namn.csv", sep=",", header=2)
```

### R

```r
# Import.
df_kvinnonamn <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/kvinnonamn.csv", sep=";")
df_mansnamn <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/mansnamn.csv", sep=";")
df_namn <- read.csv("https://raw.githubusercontent.com/peterdalle/svensktext/master/namn/namn.csv", sep=";")
```
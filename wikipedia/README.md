# Wikipedia

## Filer

6 130 751 titlar från alla svenska Wikipedia-sidor, fördelat med en fil per begynnelsebokstav (exempelvis `a.txt` för bokstaven A) för alla ord A-Ö och 0-9 samt övriga titlar sorterade under `_.txt`.

Svenska tecken som Å, Ä och Ö fungerar inte speciellt bra som filnamn och har därför fått följande namn i stället (baserade på deras HTML-tecken):

- Å = aring.txt
- Ä = auml.txt
- Ö = ouml.txt

## Datastruktur

En Wikipedia-titel per rad.

## Källa

- [Wikimedia Downloads](https://dumps.wikimedia.org/) (Ladda ned direkt: [svwiki-latest-all-titles-in-ns0.gz](http://dumps.wikimedia.org/svwiki/latest/svwiki-latest-all-titles-in-ns0.gz) 30 MB, 120 MB uppackat)

## Källkod

### Python

```py
import pandas as pd

sv_wikipedia_titles = pd.DataFrame(columns=["title"])

# Read each file into a single list.
for char in "a b c d e f g h i j k l m n o p q r s t u v w x y z aring auml ouml _ 0 1 2 3 4 5 6 7 8 9".split(" "):
    print("Reading {}...".format(char))
    df = pd.read_csv("https://github.com/peterdalle/svensktext/raw/master/wikipedia/" + char + ".txt", names=["title"]) 
    sv_wikipedia_titles = sv_wikipedia_titles.append(df)

# How many titles do we have?
print(len(sv_wikipedia_titles))

# Show tail.
sv_wikipedia_titles.tail()
```

### R

```r
# Read each file into a single list.
sv_wikipedia_titles <- NULL
for(char in c(letters, "aring", "auml", "ouml", "_", 0:9))
{
  print(paste0("Reading ", char, "..."))
  df <- read.csv(paste0("https://github.com/peterdalle/svensktext/raw/master/wikipedia/", char, ".txt"), 
                 encoding = "utf8", 
                 quote = "", 
                 sep="",
                 row.names = NULL, 
                 stringsAsFactors = FALSE,
                 header = FALSE)
  df$title <- df$V1
  df$V1 <- NULL
  sv_wikipedia_titles <- rbind(sv_wikipedia_titles, df)
}

# Set title encoding to UTF-8.
Encoding(sv_wikipedia_titles$title) <- "UTF-8"

# View.
tail(sv_wikipedia_titles$title)
```
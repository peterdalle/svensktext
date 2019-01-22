# Wikipedia

6 130 751 titlar från alla svenska Wikipedia-sidor, fördelat med en fil per begynnelsebokstav (exempelvis `a.txt` för bokstaven A) för alla ord A-Ö och 0-9 samt övriga titlar sorterade under `_.txt`.

Svenska tecken som Å, Ä och Ö fungerar inte speciellt bra som filnamn och har därför fått följande namn i stället (baserade på deras HTML-tecken):

- Å = aring.txt
- Ä = auml.txt
- Ö = ouml.txt

Källa: [Wikimedia Downloads](https://dumps.wikimedia.org/) ([svwiki-latest-all-titles-in-ns0.gz](http://dumps.wikimedia.org/svwiki/latest/svwiki-latest-all-titles-in-ns0.gz) ~30 MB, ~120 MB uppackat)

## Källkod

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
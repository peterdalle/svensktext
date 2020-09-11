# Emotioner/intensitet

Sentimentlexikon med 8 519 känsloladdade ord och deras intensitet. Uppdelade på åtta olika känslor:

- ilska
- förväntan
- avsky/äckel
- rädsla
- glädje
- vemod/sorgsenhet
- överraskning/förvåning
- tillit/förtroende

Annoterade för hand med [best-worst scaling (maximum difference scaling)](http://saifmohammad.com/WebPages/BestWorst.html).

## Filer

- anger: 1 246 ord ([CSV](anger.csv)). 
- anticipation: 813 ord ([CSV](anticipation.csv)). 
- disgust: 949 ord ([csv](disgust.csv)). 
- fear: 1 503 ord ([CSV](fear.csv)). 
- joy: 1 077 ord ([CSV](joyr.csv)). 
- sadness: 1 112 ord ([CSV](sadness.csv)). 
- surprise: 538 ord ([CSV](surprise.csv)). 
- trust: 1 281 ord ([CSV](trust.csv)). 

I katalogen [src](src/) finns originalfiler (TSV).

## Datastruktur

Notera: Ord kan förekomma bland flera emotioner (exempelvis, `mörda` är både ilska och rädsla).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`word` | Känsloord (t ex `mörda`) | Text
`intensity` | Intensitet på känslan, från `0` (låg) till `1` (hög) | Decimaltal (`#.###`)

## Källa

[The NRC Emotion Intensity Lexicon (NRC-EIL)](http://saifmohammad.com/WebPages/AffectIntensity.htm). Se källan för rättigheter vid kommersiell/icke-kommersiell användning. Referera följande papper om du använder lexikonet:

- Word Affect Intensities. Saif M. Mohammad. In *Proceedings of the 11th Edition of the Language Resources and Evaluation Conference (LREC-2018)*, May 2018, Miyazaki, Japan.

## Se även

NRC-lexikonet (och övriga lexikon från NRC) används även inom följande:

- [TidyText](https://www.tidytextmining.com/sentiment.html) - R-paket för textanalys där NRC-lexikonet finns inbyggt (se också [Syuzhet](https://cran.r-project.org/web/packages/syuzhet/vignettes/syuzhet-vignette.html)-paketet).
- [lexicon](https://cran.r-project.org/web/packages/lexicon/index.html) - R-paket för NRC-lexikonet.
- [Shifterator](https://github.com/ryanjgallagher/shifterator) - Python-bibliotek för "interpretable data visualizations for understanding how texts differ at the word level".
- [AffectiveTweets](https://github.com/felipebravom/AffectiveTweets) - Java-bibliotek, mer specifikt "A WEKA package for analyzing emotion and sentiment of tweets".

## Källkod

### R

```r
# Import.
get_emotions <- function(emotion = NULL) {
  valid_emotions <- c("anger", "anticipation", "disgust", "fear", "joy", "sadness", "surprise", "trust")
  if (is.null(emotion)) {
    # Get all emotions.
    df <- data.frame(word=NULL, intensity=NULL, emotion=NULL)
    for (emotion in valid_emotions) {
      url <- paste0("https://github.com/peterdalle/svensktext/raw/master/emotioner/", emotion, ".csv")
      df_emotion <- read.csv(url, na.strings="None", encoding="UTF-8", header=TRUE, sep=",", stringsAsFactors=FALSE)
      df_emotion$emotion <- emotion
      df <- rbind(df, df_emotion)
    }
    return(df)
  } else {
    # Get single emotion.
    if (!(emotion %in% valid_emotions)) {
      stop(paste0("'", emotion, "' is an invalid emotion. Must be one of: ", paste(valid_emotions, collapse=", "), "."), call.=FALSE)
    }
    url <- paste0("https://github.com/peterdalle/svensktext/raw/master/emotioner/", emotion, ".csv")
    df <- read.csv(url, na.strings="None", encoding="UTF-8", header=TRUE, sep=",", stringsAsFactors=FALSE)
    df$emotion <- emotion
    return(df)
  }
}

# Get all emotions.
df <- get_emotions()
head(df)

# Get single emotion.
df <- get_emotions(emotion = "fear")
head(df)
```
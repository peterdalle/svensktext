# Slår ihop alla separata TXT-filer med myndigheter till en gemensam TSV-fil.
# Därefter gjordes lite manuell tvätt av TSV-filen.

library(stringr)
library(tidyverse)

myndighet <- read.csv("AP-fonder.txt", sep="\t", header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE)
apfonder <- data.frame(
  type = "AP-fond",
  name = stringr::str_to_sentence(myndighet$Namn),
  city = stringr::str_to_title(myndighet$BesöksPostOrt),
  country = "Sverige")
apfonder$name <- stringr::str_replace(apfonder$name, "ap", "AP")

myndighet <- read.csv("Myndigheter under riksdagen.txt", sep="\t", header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE)
underriksdagen <- data.frame(
  type = "Myndighet under riksdagen",
  name = stringr::str_to_sentence(myndighet$Namn),
  city = stringr::str_to_title(myndighet$BesöksPostOrt),
  country = "Sverige")

myndighet <- read.csv("Statliga affärsverk.txt", sep="\t", header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE)
affarsverk <- data.frame(
  type = "Statligt affärsverk",
  name = stringr::str_to_sentence(myndighet$Namn),
  city = stringr::str_to_title(myndighet$BesöksPostOrt),
  country = "Sverige")

myndighet <- read.csv("Statliga förvaltningsmyndigheter.txt", sep="\t", header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE)
forvaltning <- data.frame(
  type = "Statlig förvaltningsmyndighet",
  name = stringr::str_to_sentence(myndighet$Namn),
  city = stringr::str_to_title(myndighet$BesöksPostOrt),
  country = "Sverige")

myndighet <- read.csv("Svenska utlandsmyndigheter.txt", sep="\t", header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE)
myndighet <- myndighet %>%
  filter(!str_starts(Namn, "se ")) %>%
  filter(!str_starts(Namn, "Se ")) %>%
  filter(!is.na(Namn) & Namn != "" & !is.null(Namn))
utland <- data.frame(
  type = "Utlandsmyndighet",
  name = myndighet$Namn,
  city = "",
  country = myndighet$Land)

myndighet <- read.csv("Sveriges domstolar samt Domstolsverket.txt", sep="\t", header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE)
domstolar <- data.frame(
  type = "Domstol",
  name = stringr::str_to_sentence(myndighet$Namn),
  city = stringr::str_to_title(myndighet$BesöksPostOrt),
  country = "Sverige")

#myndighet <- read.csv("Svenska utlandsmyndigheter.txt", sep="\t", header=TRUE, encoding="UTF-8", stringsAsFactors=FALSE)
#myndighet <- myndighet %>%
#  filter(!str_starts(Namn, "se ")) %>%
#  filter(!str_starts(Namn, "Se ")) %>%
#  filter(!is.na(Namn) & Namn != "" & !is.null(Namn))
#utland <- data.frame(
#  type = "Utlandsmyndighet",
#  name = myndighet$Namn,
#  city = "",
#  country = myndighet$Land)

# Slå ihop till en enskild fil.
df <- rbind(apfonder, underriksdagen, affarsverk, forvaltning, domstolar)
write.table(df, file="myndigheter.tsv", sep="\t", row.names=FALSE, fileEncoding="UTF-8", quote=FALSE)

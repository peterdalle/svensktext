# Platser

## Svenska orter

2 007 namn på svenska orter ([JSON](ortsnamn.json)).

Källa: [Mattias Hising](https://github.com/hising/svensk-data)

## Sveriges län

Sveriges 21 län ([CSV](lan.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`name` | Namnet på länet | Text
`letter` | Länsbokstav | Text
`code` | Länskod | Text
`area` | Yta | Heltal
`population` | Folkmängd (2018-03-31) | Heltal
`population_per_square_km` | Invånare per kvadratkilometer | Decimaltal
`residencetown` | Residensstad | Text
`municipalities` | Antal kommuner i länet | Heltal
`founded ` | Året då länet inrättades | Text
`order_from_north_to_south` | Ordningen från norr till söder (residensstad) | Heltal

Källa: [Wikipedia - Sveriges län](https://sv.wikipedia.org/wiki/Sveriges_l%C3%A4n#Lista_%C3%B6ver_Sveriges_l%C3%A4n)

## Sveriges kommuner

Sveriges 290 kommuner ([CSV](kommuner.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`code` | Kommunkod | Tal
`name` | Kommunens namn | Text
`region` | Län | Text
`population` | Folkmängd | Decimaltal
`area` | Total areal, kvadratkilometer | Decimaltal
`land` | Landareal, kvadratkilometer | Decimaltal
`sea` | Inlandsvattenareal, exklusive fyra största sjöarna, kvadratkilometer | Decimaltal
`ocean` | Havsvattenareal, kvadratkilometer | Decimaltal
`density` | Befolkningstäthet, invånare per kvadratkilometer land | Decimaltal
`bounds_ne_lat_google_2015_05_28` |  | Decimaltal
`bounds_ne_lng_google_2015_05_28` |  | Decimaltal
`bounds_sw_lat_google_2015_05_28` |  | Decimaltal
`bounds_sw_lng_google_2015_05_28` |  | Decimaltal
`location_lat_google_2015_05_28` |  | Decimaltal
`location_lng_google_2015_05_28` |  | Decimaltal

Data städad genom att göra om header till engelska namn samt ta bort mellanslag som tusentalavgränsare.

Källa: [Marcus Asplund](https://github.com/marcusasplund/kommundata)

## Länder och huvudstäder

Världens 199 länder samt deras huvudstäder ([CSV](lander.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
 `country` | Namnet på landet | Text
 `capital` | Namnet på huvudstaden | Text

Källa: [Världens flaggor](http://www.flaggorvarlden.se/lista)

## Landskoder

245 landskoder i ISO 3166-1-format ([CSV](landskoder.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`code2` | Landskod i versaler om 2 bokstäver | Text
`code3` | Landskod i versaler om 3 bokstäver | Text
`number` | Nummer på land om 3 siffror | Tal
`country` | Namnet på landet | Text

Källa: [ISO 3166-1-koder](https://sv.wikipedia.org/wiki/ISO_3166)
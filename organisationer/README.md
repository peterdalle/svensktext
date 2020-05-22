# Organisationer

## Nyhetsmedier

### Filer

- 158 domäner till svenska nyhetsmedier ([CSV](massmedier-nyheter-domaner.csv))
- 20 domäner till internationella sociala medier ([CSV](sociala-medier-domaner.csv))

### Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`domain` | Domännamn utan subdomän (exempelvis dn.se) | Text

### Källa

- [Wikipedia](https://en.wikipedia.org/wiki/Social_media)
- Nyhetsmedier från [#svpol](https://twitter.com/search?q=%23svpol&src=typd)

## Myndigheter

### Filer

- 354 svenska myndigheter ([TSV](myndigheter.tsv))

Svenska ambassader är inte med eftersom de består av variationer av samma fras (exempelvis "Sveriges ambassad i Berlin").

### Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`type` | En av fem kategoriseringar av myndigheterna enligt SCB (`AP-fond`, `Myndighet under riksdagen`, `Statligt affärsverk`, `Statlig förvaltningsmyndighet` eller `Domstol`) | Text
`name` | Svenskt namn på myndigheten | Text
`city` | Stad där myndigheten finns | Text

### Källa

- [Myndighetsregistret SCB](http://www.myndighetsregistret.scb.se/)

## EU:s institutioner och organ

### Filer

Filen [eu.csv](eu.csv) innehåller 17 namn på EU:s institutioner och organ,

### Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`name` | Namn på organisation | Text
`alternative_name` | Alternativt namn på organisation | Text
`acronym` | Förkortning av namnet eller annan vanlig typ av förkortning | Text

### Källa

- [EU:s institutioner och andra organ](https://europa.eu/european-union/about-eu/institutions-bodies_sv)
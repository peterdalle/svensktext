# Tider

## Helgdagar

### Filer

- 23 helgdagar ([TXT](helgdagar.txt)).

### Datastruktur

En helgdag per rad.

### Källa

- https://sv.wikipedia.org/wiki/Helgdagar_i_Sverige

## Tidsperioder

### Filer

- 19 tidsperioder ([CSV](tidsperioder.csv)).

### Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`name` | Namnet på tidsperioden (t ex `dygn`) | Text
`duration` | Varaktighet på tidsperioden i läsbar form (t ex `24 timmar`) | Text
`duration_seconds` | Varaktighet på tidsperioden i sekunder (t ex `86400`) | Heltal

### Källa

- https://sv.wikipedia.org/wiki/Tidsperiod

## Månader

### Filer

- 12 månader ([CSV](manader.csv))

### Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`number` | Månadens nummer, 1 till 12 | Heltal
`name` | Namnet på månaden | Text

## Veckodag

### Filer

- 7 veckodagar ([CSV](veckodagar.csv))

### Datastruktur

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`number` | Veckodagens nummer, 1 till 7 | Heltal
`name` | Namnet på veckodagen | Text
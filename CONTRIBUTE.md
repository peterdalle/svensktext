# Bidra med data

Bidra med egen data genom att följa dessa riktlinjer.

## Licens

- Filerna måste vara fria att använda utan begränsningar
- Alla som bidrar ska bli uppmärksammade för sina bidrag

## Format

- CSV
- JSON

Katalogen `src` som finns inuti en del kataloger innehåller kod för att konvertera originalfiler (exempelvis till CSV). Var noga med att antingen ta med originalfilerna (om licensen tillåter det) eller beskriva hur originalfilerna kan hämtas!

## Dokumentation

### CSV

- i första hand komma-separerad, i andra hand semikolon-separerad, i tredje hand tab-separerad
- headers på första raden (gemener, på engelska)
- dokumentera vad varje header betyder (samt dess datatyp)
- UTF-8 teckenkodning

### Datatyper

Använd ett enkelt språkbruk (decimaltal, heltal, datum, text, lista) och undvik att använda namnet på programspecifika datatyper.

Datatyp | Exempel | Beskrivning | Variabeltyper
:------ | :------------ | :------------------- | :------
Decimaltal | 3.7 | skriv alltid med punkt | float
Heltal | 3 | | integer, int
Datum | 2019-01-01 | skrivs alltid i standardiserat format, såsom `yyyy-mm-dd` eller `yyyy-mm-dd hh:mm:ss` | date, datetime
Text | "Namn" | inom citationstecken | string, str
Lista | [1, 2, 3] | i detta fall innehåller listan tal | list, array, vector
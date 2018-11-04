# Bidra med data

Bidra med egen data genom att följa dessa riktlinjer.

## Licens

Filerna måste vara fria att använda utan begränsningar.

Däremot ska alla som bidrar bli uppmärksammade för sina bidrag.

## Format

Erbjud CSV och JSON.

## Dokumentation

### CSV

- använd komma-separerad CSV i första hand, i andra hand ;-separerad, i tredje hand tab-separerad
- använd headers på första raden (gemener, på engelska)
- förklara vad varje header betyder
- förklara datatypen för varje header

### Datatyper

Använd ett enkelt språkbruk (decimaltal, heltal, datum, text, lista) och undvik att använda namnet på programspecifika datatyper.

Datatyp | Exempel | Beskrivning | Variabeltyper
:------ | :------------ | :------------------- | :------
Decimaltal | 3.7 | skriv alltid med punkt | float
Heltal | 3 | | integer, int
Datum | 2019-01-01 | skrivs alltid i standardiserat format, såsom `yyyy-mm-dd` eller `yyyy-mm-dd hh:mm:ss` | date, datetime
Text | "Namn" | inom citationstecken | string, str
Lista | [1, 2, 3] | i detta fall innehåller listan tal | list, array, vector
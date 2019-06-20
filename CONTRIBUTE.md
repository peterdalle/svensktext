# Bidra med data

Bidra med egen data genom att följa dessa riktlinjer.

## Licens

- Filerna måste vara fria att använda utan begränsningar
- Alla som bidrar ska bli uppmärksammade för sina bidrag

## Format

- TXT
- CSV
- JSON

Katalogen `src` som finns inuti en del kataloger innehåller kod för att konvertera originalfiler (exempelvis till CSV). Var noga med att antingen ta med originalfilerna (om licensen tillåter det) eller beskriva hur originalfilerna kan hämtas.

## Dokumentation

### TXT

- när du bara behöver en enkel lista (alltså en variabel)
- UTF-8 teckenkodning

### CSV

- i första hand komma-separerad, i andra hand semikolon-separerad, i tredje hand tab-separerad
- headers på första raden - gemener på engelska (exempelvis `country,currency,country_code`)
- dokumentera vad varje header betyder samt datatyp (exempelvis `Text`, `Heltal`, `Decimaltal`, `Datum`)
- UTF-8 teckenkodning

### JSON

- använd JSON då CSV inte räcker till
- försök hålla en så platt struktur som möjligt (få nästlade element)
- namn på nycklar skrivs med gemener på engelska, använd underscore vid behov (exempelvis `country_code`)
- UTF-8 teckenkodning

### Datatyper

Beskriv variablernas datatyp med ett enkelt språkbruk (decimaltal, heltal, datum, text, lista). Undvik programspecifika datatyper.

Datatyp | Exempel | Beskrivning | Variabeltyper
:------ | :------------ | :------------------- | :------
Decimaltal | 3.7 | skriv decimaltal med punkt | float, decimal
Heltal | 3623 | undvik tusentalsavgränsare | integer, int, int32, int64
Datum | 2019-01-01 | skrivs alltid i standardiserat format (`yyyy-mm-dd` eller `yyyy-mm-dd hh:mm:ss`) | date, datetime
Text | "Namn" | inom citationstecken | string, str
Lista | [1, 2, 3] | i detta fall innehåller listan tal | list, array, vector
# Nationaliteter

197 nationaliteter med namn på invånarna i landet, både singular och plural ([JSON](nationaliteter.json), [CSV](nationaliteter.csv)).

Kolumn | Beskrivning | Datatyp
:------- | :----------  | :----------
`id` | Godtyckligt ID på landet (från 0 till 196)  | Heltal
`country` | Namnet på landet (t.ex. Storbritannien) | Text
`country_alternativename` | Alternativt namn på landet | Text
`resident_singular` | Vad invånarna kallas i singular (t.ex. britt) | ['Lista']
`resident_plural` | Vad invånarna kallas i plural (t.ex. britter) | ['Lista']
`adjective` | Vad invånarna kallas som adjektiv (t.ex. brittisk) | Text

Källa: [TT-språket](https://tt.se/tt-spraket/ord-och-begrepp/internationellt/stat-och-nationalitet/)
import pandas as pd

# Läs in CSV-filen med är kopierad från TT-språkets sida
# https://tt.se/tt-spraket/ord-och-begrepp/internationellt/stat-och-nationalitet/
# första tabellen
data = pd.read_csv("nationaliteter/nationaliteteter-ttspraket.csv")

# Parsa textsträng med singularformen av nationalitet, såsom "vitryss (-ar)",
# och skapa singularform och pluralform separerade, det vill säga "vitryss"
# respektive "vitryssar".
def get_plural_names(names):
    sing = []
    plur = []
    for name in names.split(","):
        if name.find("(=)") > -1:
            singular = name.replace("(=)", "")
            plural = singular
        elif name.find("(-er)") > -1:
            singular = name.replace(" (-er)", "")
            plural = name.replace(" (-er)", "er")
        elif name.find("(-ar)") > -1:
            singular = name.replace(" (-ar)", "")
            plural = name.replace(" (-ar)", "ar")
        elif name.find("(finnar)") > -1:
            singular = "finne"
            plural = "finnar"
        elif name.find("fransman") > -1:
            singular = "fransman"
            plural = "fransmän"
        elif name.find("myanmarier") > -1:
            singular = "myanmarier"
            plural = "myanmarier"
        elif name.find("norrman") > -1:
            singular = "norrman"
            plural = "norrmän"
        else:
            raise ValueError("Hittade något som inte stöds än: " + names)
        sing.append(singular.strip())
        plur.append(plural.strip())
    return(sing, plur)

# Gör en lista med singularformen som passar data framens antal rader.
def make_singulars():
    l = []
    for names in data["resident_singular"]:
        sing, plur = get_plural_names(names)
        l.append(sing)
    return(l)

# Gör en lista med pluralformen som passar data framens antal rader.
def make_plurals():
    l = []
    for names in data["resident_singular"]:
        sing, plur = get_plural_names(names)
        l.append(plur)
    return(l)

# Måste spara i separata variabler eftersom funktionerna läser direkt från data framen.
singulars = make_singulars()
plurals = make_plurals()

# Skriv listorna till data framen.
data["resident_singular"] = singulars
data["resident_plural"] = plurals

# Spara till json eftersom singular-/pluralformerna är nästlade.
data.to_json("nationaliteter/nationaliteteter.json")
sentences = [
    "Serveris neatsako",
    "Šiandien labai lyja",
    "Man patinka valgyti picą",
    "Važiuoju į darbą autobusu",
    "Aš kasdien bėgioju ryte",
    "Kompiuteris šiandien veikia lėtai",
    "Ši sriuba labai skani",
    "Traukinys vėlavo trisdešimt minučių",
    "Sportas gerina savijautą",
    "Rytoj bus saulėta diena",
    "Man patinka programuoti Python kalba",
    "Kava yra per karti",
    "Kelionė automobiliu buvo ilga",
    "Sveika mityba yra svarbi",
    "Debesys dengia dangų",
    "Programinė įranga buvo atnaujinta",
    "Makaronai su sūriu yra puikūs",
    "Taksi atvyko greitai",
    "Aš pavargau po treniruotės",
    "Vasarą dažnai būna karšta",
    "Ši programa turi klaidų",
    "Ledai vasarą yra nuostabūs",
    "Autobusas buvo pilnas žmonių",
    "Reikia daugiau miegoti",
    "Oras yra šaltas ir vėjuotas",
    "Duomenų analizė yra įdomi",
    "Man patinka keliauti traukiniu",
    "Jis valgo daug daržovių",
    "Pučia stiprus vėjas",
    "Šokoladas yra mano mėgstamiausias desertas",
    "Aš mokausi mašininio mokymosi",
    "Kelionė buvo labai varginanti",
    "Vaikščiojimas gryname ore yra naudingas",
    "Žiema šiemet labai šalta",
    "Internetas yra labai greitas",
    "Ar noriu arbatos ar kavos?",
    "Aš dažnai skrendu į užsienį",
    "Man patinka šiltas oras",
    "Dirbu su dirbtiniu intelektu",
    "Ši pica yra labai skani",
    "Sveikata yra svarbiausia",
    "Oras šiandien puikus",
    "Kodas neveikia kaip tikėtasi",
    "Lėktuvas pakilo laiku",
    "Man nepatinka ši kava",
    "Aš stengiuosi gyventi sveikai",
    "Važiuoti dviračiu yra smagu",
    "Man patinka sportuoti salėje",
    "Lauke sninga",
    "Aš mėgstu itališką maistą"
]

expected_labels = [
    2,  # Serveris neatsako
    4,  # Šiandien labai lyja
    0,  # Man patinka valgyti picą
    1,  # Važiuoju į darbą autobusu
    3,  # Aš kasdien bėgioju ryte
    2,  # Kompiuteris šiandien veikia lėtai
    0,  # Ši sriuba labai skani
    1,  # Traukinys vėlavo trisdešimt minučių
    3,  # Sportas gerina savijautą
    4,  # Rytoj bus saulėta diena
    2,  # Man patinka programuoti Python kalba
    0,  # Kava yra per karti
    1,  # Kelionė automobiliu buvo ilga
    3,  # Sveika mityba yra svarbi
    4,  # Debesys dengia dangų
    2,  # Programinė įranga buvo atnaujinta
    0,  # Makaronai su sūriu yra puikūs
    1,  # Taksi atvyko greitai
    3,  # Aš pavargau po treniruotės
    4,  # Vasarą dažnai būna karšta
    2,  # Ši programa turi klaidų
    0,  # Ledai vasarą yra nuostabūs
    1,  # Autobusas buvo pilnas žmonių
    3,  # Reikia daugiau miegoti
    4,  # Oras yra šaltas ir vėjuotas
    2,  # Duomenų analizė yra įdomi
    1,  # Man patinka keliauti traukiniu
    3,  # Jis valgo daug daržovių
    4,  # Pučia stiprus vėjas
    0,  # Šokoladas yra mano mėgstamiausias desertas
    2,  # Aš mokausi mašininio mokymosi
    1,  # Kelionė buvo labai varginanti
    3,  # Vaikščiojimas gryname ore yra naudingas
    4,  # Žiema šiemet labai šalta
    2,  # Internetas yra labai greitas
    0,  # Ar noriu arbatos ar kavos?
    1,  # Aš dažnai skrendu į užsienį
    4,  # Man patinka šiltas oras
    2,  # Dirbu su dirbtiniu intelektu
    0,  # Ši pica yra labai skani
    3,  # Sveikata yra svarbiausia
    4,  # Oras šiandien puikus
    2,  # Kodas neveikia kaip tikėtasi
    1,  # Lėktuvas pakilo laiku
    0,  # Man nepatinka ši kava
    3,  # Aš stengiuosi gyventi sveikai
    1,  # Važiuoti dviračiu yra smagu
    3,  # Man patinka sportuoti salėje
    4,  # Lauke sninga
    0   # Aš mėgstu itališką maistą
]
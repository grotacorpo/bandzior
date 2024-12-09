import json

# Wczytaj CzarnaWiedza
def wczytaj_biblioteke():
    with open("czarna_wiedza.json", "r") as file:
        return json.load(file)

# Zapisz notatkę do biblioteki
def zapisz_do_biblioteki(note):
    data = wczytaj_biblioteke()
    data["library"].append(note)
    with open("czarna_wiedza.json", "w") as file:
        json.dump(data, file, indent=4)
    print(f"[Biblioteka]: {note}")

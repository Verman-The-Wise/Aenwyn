import os
import shutil

I_b = "element/chronicle.kv"
I_p = "element/projects.kv"
O = "to-world"

os.makedirs(O, exist_ok=True) # creates the output DIR.
shutil.copy("style.css", O)   # copies the style.css to output DIR.
def parse_kv():

    glossary = []
    BLOK = {}
    last_key = None

    with open(I_b, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                if BLOK:
                    glossary.append(BLOK)
                    BLOK = {}
                    last_key = None
                continue
            if ' : ' in line:
                key, value = line.split(" : ", 1)
                BLOK[key] = value
                last_key = key
            else:
                if last_key:
                    BLOK[last_key] = f"{BLOK[last_key]}\n{line}"
        if BLOK:
            glossary.append(BLOK)

    return glossary
        
base_data = parse_kv()

def parse_project():

    glossary = []
    BLOK = {}
    last_key = None

    with open(I_p, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                if BLOK:
                    glossary.append(BLOK)
                    BLOK = {}
                    last_key = None
                continue
            if ' : ' in line:
                key, value = line.split(" : ", 1)
                BLOK[key] = value
                last_key = key
            else:
                if last_key:
                    BLOK[last_key] = f"{BLOK[last_key]}\n{line}"
        if BLOK:
            glossary.append(BLOK)

    return glossary
        
proj_data = parse_project()


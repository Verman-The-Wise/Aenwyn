import os
import shutil

I = "element/chronicle.kv"
O = "to-world"

os.makedirs(O, exist_ok=True) # creates the output DIR.
shutil.copy("style.css", O)   # copies the style.css to output DIR.

def parse_kv():

    glossary = []
    BLOK = {}
    last_key = None

    with open(I, "r") as file:
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
        
data = parse_kv()

def write_data(glossary):
    for BLOK in glossary:
        title = BLOK.get("TITL", "Untitled")
        description = BLOK.get("BODY", "No content available.")
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<h2>{title}</h2>
<main>
{description}
<footer><p>Aenwyn</p></footer>
</main>
</body>
</html>
"""
        url = title.replace(' ', '-').lower() + ".html"
        with open(os.path.join(O, url), "w", encoding='utf-8') as h:
            h.write(html)
        print(url)
    
def main():
    write_data(data)
    
main()

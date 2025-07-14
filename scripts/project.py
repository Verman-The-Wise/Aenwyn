import os

I = "element/projects.kv"
O = "to-world"

def parse_project():

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
        
data = parse_project()

def write_data(glossary):
    for BLOK in glossary:
        title = BLOK.get("TITL", "Untitled")
        description = BLOK.get("BODY", "No content available.")

        with open("layout/base.html", "r") as file:
            template_base = file.read()
        
        html_base = template_base.format(title = title, description = description) 

        url = title.replace(' ', '-').lower() + ".html"
        with open(os.path.join(O, url), "w", encoding='utf-8') as h:
            h.write(html_base)
        print(url)
    
def main():
    write_data(data)
    
main()
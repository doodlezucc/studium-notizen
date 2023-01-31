import io
import os
import unicodedata

def insert_title_header_all(root):
    for child in os.listdir(root):
        child_path = os.path.join(root, child)

        if os.path.isfile(child_path):
            # is file -> fix markdown title
            insert_title_header(child_path)
        else:
            # is directory -> traverse deeper
            insert_title_header_all(child_path)


def insert_title_header(path: str):
    if not path.endswith(".md"):
        return
    
    with io.open(path, mode="r", encoding="UTF8") as file:
        content = file.read()
        if (content.lstrip().startswith("# ")):
            return
        
        name = os.path.basename(path)[0:-3]
        name = unicodedata.normalize("NFC", name)

        content = "# " + name + "\n" + content
        print(name)
    
    with io.open(path, mode="w", encoding="UTF8") as file:
        file.write(content)


insert_title_header_all("wiki")
import os
from acdh_tei_pyutils.utils import TeiReader

data_dir = "data"
dirs = ["editions", "indices"]
for x in dirs:
    os.makedirs(os.path.join(data_dir, x), exist_ok=True)

doc = TeiReader("https://karl-kraus.github.io/legalkraus-static/D_000002-003-000.xml")


for x in doc.any_xpath(".//tei:lb | .//tei:p | .//tei:pb"):
    try:
        del x.attrib["{http://www.w3.org/XML/1998/namespace}id"]
    except:
        pass

doc.tree_to_file("./data/editions/D_000002-003-000.xml")


register_files = {
    "listperson.xml": {
        "title": "Personenregister",
        "xpath": ".//tei:back//tei:listPerson"
    },
    "listplace.xml": {
        "title": "Ortsregister",
        "xpath": ".//tei:back//tei:listPlace"
    },
    "listorg.xml": {
        "title": "Organisationsregister",
        "xpath": ".//tei:back//tei:listOrg"
    },
    "listbibl.xml": {
        "title": "Werksverzeichniz",
        "xpath": ".//tei:back//tei:listBibl"
    },
}

dummy_str = """
<TEI xmlns="http://www.tei-c.org/ns/1.0">
    <teiHeader>
        <fileDesc>
            <titleStmt>
                <title type="main">Werkverzeichnis</title>
            </titleStmt>
            <publicationStmt>
                <p />
            </publicationStmt>
            <sourceDesc>
                <p>born digital</p>
            </sourceDesc>
        </fileDesc>
    </teiHeader>
    <text>
        <body>
            <div/>
        </body>
    </text>
</TEI>
"""


for key, value in register_files.items():
    dummy = TeiReader(dummy_str)
    div = dummy.any_xpath(".//tei:div")[0]
    index = doc.any_xpath(value["xpath"])[0]
    div.append(index)
    dummy.tree_to_file(os.path.join(data_dir, "indices", key))
import os
from acdh_tei_pyutils.utils import TeiReader

doc = TeiReader("https://arthur-schnitzler.github.io/schnitzler-bahr-static/L041464.xml")
data_dir = "data"
for bad in doc.any_xpath(".//tei:titleStmt/tei:title[@level='s']"):
    bad.getparent().remove(bad)
doc.tree_to_file(os.path.join(data_dir, "editions", "L041464.xml"))


register_files = {
    "listperson.xml": {
        "title": "Personenregister",
        "xpath": ".//tei:back//tei:listPerson/tei:person",
        "nxpath": ".//tei:listPerson"
    },
    "listplace.xml": {
        "title": "Ortsregister",
        "xpath": ".//tei:back//tei:listPlace/tei:place",
        "nxpath": ".//tei:listPlace"
    },
    "listorg.xml": {
        "title": "Organisationsregister",
        "xpath": ".//tei:back//tei:listOrg/tei:org",
        "nxpath": ".//tei:listPlace"
    },
    "listbibl.xml": {
        "title": "Werksverzeichniz",
        "xpath": ".//tei:back//tei:listBibl/tei:bibl",
        "nxpath": ".//tei:listBibl"
    },
}


for key, value in register_files.items():
    dummy = TeiReader(os.path.join(data_dir, "indices", key))
    try:
        list_whatever = dummy.any_xpath(value["nxpath"])[0]
    except IndexError:
        continue
    index = doc.any_xpath(value["xpath"])
    for x in index:
        list_whatever.append(x)
    dummy.tree_to_file(os.path.join(data_dir, "indices", key))
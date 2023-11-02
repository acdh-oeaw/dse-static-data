import os
from acdh_tei_pyutils.utils import TeiReader

doc = TeiReader("https://donauhandel.github.io/wkfm-static/wkfm-0023.xml")
base = doc.any_xpath("//tei:TEI")[0]
del base.attrib["next"]
data_dir = "data"

url_prefix = "https://id.acdh.oeaw.ac.at/wkfm/"

for x in doc.any_xpath(".//tei:graphic"):
    url = x.attrib["url"]
    x.attrib["url"] = f"{url_prefix}{url}"

for x in doc.any_xpath(".//tei:pb"):
    del x.attrib["corresp"]

for bad in doc.any_xpath(".//tei:noteGrp"):
    bad.getparent().remove(bad)

doc.tree_to_file(os.path.join(data_dir, "editions", "wkfm-0023.xml"))

persons = doc.any_xpath(".//tei:back//tei:person")
    
listperson_file = "./data/indices/listperson.xml"
doc = TeiReader(listperson_file)
listperson_node = doc.any_xpath(".//tei:listPerson")[0]
for x in persons:
    listperson_node.append(x)

doc.tree_to_file(listperson_file)




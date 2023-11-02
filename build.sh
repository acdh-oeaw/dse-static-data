python legalkraus_sample.py
python wkfm_sample.py
python hbas_sample.py

add-attributes -g "data/editions/*.xml" -b "https://id.acdh.oeaw.ac.at/dse-static"
denormalize-indices -f "./data/editions/*.xml" -i "./data/indices/*.xml" -m ".//*[@ref]/@ref" -x ".//tei:titleStmt/tei:title[1]/text()"
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Invert Stumpf 2 pages dict
"""

import os.path
import json

def main():
    here = os.path.dirname(__file__)
    pagesfilename = os.path.join(here, "..", "data", "stumpf_2_pages.json")
    with open(pagesfilename) as infile:
        d = json.load(infile)
    out = {}
    pages = d["pages"]
    for page in pages:
        for docnum in pages[page]["docnums"]:
            out[docnum] = {
                "url": pages[page]["url"],
                "page": page,
            }
    docsfilename = os.path.join(here, "..", "data", "stumpf_2_docs.json")
    with open(docsfilename, "w") as outfile:
        json.dump(out, outfile, indent=2)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import re

old_id = r"-?(?:(?:[a-z]+(?:.[a-z]+)/)?[0-9]{4}[0-9]+)"
new_id = r"(?:[0-9]{4}.[0-9]+)(?:v[0-9]+)?"
arxiv_prefixes = r"(?:{0})".format("|".join([
    "(?:arxiv[=|:])", 
    "(?://arxiv\.org/(?:(?:abs/)|(?:pdf/))?)"]))
pmc_prefixes = r"(?:{0})".format("|".join([
    r"pmc=(?:pmc)?", 
    r"(?:ncbi\.nlm\.nih\.gov/pmc/articles/pmc)"]))
pmid_prefixes = r"(?:{0})".format("|".join([
    r"pmid=(?:pmc)?", 
    r"(?:ncbi\.nlm\.nih\.gov/pubmed/)"]))

dict_of_ids = {
    'doi' : re.compile(r"""[=:]?(10\.\d+(?:/|(?:%2f))[^\s|&,"'?![\]<>{}]+)"""),
    #'isbn' : re.compile(r"""[=|:/]?(?:(?:\d+-?)?97(?:[89])-?)?(\d(?:-?\d){8})"""),
    'isbn' : re.compile(r"""isbn[=|:/]?(?:(?:\d+-?)?97(?:[89])-?)?(\d(?:-?\d){9})"""),
    #'issn' : re.compile(r"""[=|:/]?(?:977-?)?((?:-?\d){4}\-(?:-?\d){3})"""),
    'issn' : re.compile(r"""issn[=|:/]?(?:977-?)?((?:\d){4}\-(?:\d){4})"""),
    'arxiv' : re.compile(arxiv_prefixes + r"((?:{0})|(?:{1}))".format(old_id, new_id)),
    'pmc' : re.compile(pmc_prefixes + r"([\d]+)"),
    'pmid' : re.compile(pmid_prefixes + r"([\d]+)")
}


# coding: utf8
from __future__ import unicode_literals
from spacy.symbols import (
    POS,
    ADJ,
    ADP,
    ADV,
    AUX,
    CCONJ,
    DET,
    INTJ,
    NOUN,
    NUM,
    PART,
    PRON,
    PROPN,
    PUNCT,
    SCONJ,
    VERB,
    X,
)


# fmt: off
custom_tag_map = {
    "ADJ": {POS: ADJ},
    "ADJA": {POS: ADJ}, 
    "ADJA": {POS: ADJ},
    "ADJC": {POS: ADJ},
    "ADJP": {POS: ADJ},
    "ADV": {POS: ADV},
    "AGLT": {POS: AUX},
    "BEDZIE": {POS: VERB},
    "BREV": {POS: X},
    "BURK": {POS: ADV},
    "COMP": {POS: SCONJ},
    "CONJ": {POS: CCONJ},
    "DEPR": {POS: NOUN},
    "FIN": {POS: VERB},
    "GER": {POS: NOUN},
    "IMPS": {POS: VERB},
    "IMPT": {POS: VERB},
    "INF": {POS: VERB},
    "INTERJ": {POS: INTJ},
    "INTERP": {POS: PUNCT},
    "NUM": {POS: NUM},
    "NUMCOL": {POS: NUM},
    "PACT": {POS: VERB},
    "PANT": {POS: VERB},
    "PCON": {POS: VERB},
    "PPAS": {POS: VERB},
    "PPRON12": {POS: PRON},
    "PPRON3": {POS: PRON},
    "PRAET": {POS: VERB},
    "PRED": {POS: VERB},
    "PREP": {POS: ADP},
    "QUB": {POS: PART},
    "SIEBIE": {POS: PRON},
    "SUBST": {POS: NOUN},
    "WINIEN": {POS: VERB},
    "XXX": {POS: X}}

# fmt: on

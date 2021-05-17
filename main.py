#! /usr/bin/env python3

from docx2python import docx2python
from docx2python.iterators import enum_at_depth
from pprint import pprint
from preprocess import clean, transform

f = docx2python('Avengers.docx')

# ready_f is a list of sets
ready_f = transform(clean(f))
pprint(ready_f)

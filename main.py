#! /usr/bin/env python3

from docx2python import docx2python
from docx2python.iterators import enum_at_depth
from pprint import pprint
from preprocess import clean, transform
from logic import gen_nonconflict_report
import json

f = docx2python('Avengers.docx')

# ready_f is a list of sets
ready_f = transform(clean(f))

nonconflicts, stats = gen_nonconflict_report(ready_f)

with open("results/stats.json", "w") as outfile:
    processed = [{'keys': k, 'times': v, 'non-conflicts': ",".join(nonconflicts[k])} for k, v in stats.items()]
    json.dump(processed, outfile, indent=4)


from docx2python.iterators import docx2python
from docx2python.iterators import enum_at_depth

f = docx2python('Avengers.docx')

for i in range(len(f[1])):
    print(f.body[1][i])

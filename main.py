from docx2python import docx2python
from docx2python.iterators import enum_at_depth
from functools import reduce

f = docx2python('Avengers.docx')
ANGKLUNG_SIGN = 'Ang.'
akl_idx = []

# assumption: all instruments have same length
def flip_axes(l):
    res = []
    for i in range(len(l[0])):
        res.append([])
        for j in range(len(l)):
            res[i].append(l[j][i])
    return res

def flatten(input):
    return [
        reduce(lambda x, y: x + y, row, []) 
        for row in input
    ]

# which lines belong to angklung?
# each lines is represented as a tuple of indexes 
# where left idx inclusive, right idx exclusive
def find_angklung_index(input):
    # index of non-separator lines
    nonsep_idx = [i for i, row in enumerate(input) if ''.join(row) != '']
    angklung_idx = [i for i, row in enumerate(input) if row[0] == ANGKLUNG_SIGN]

    res = []
    for i in angklung_idx:
        start = nonsep_idx.index(i)
        l, r = start - 1, start + 1
        while l >= 0 and nonsep_idx[l + 1] == nonsep_idx[l] + 1:
            l -= 1
        while r < len(nonsep_idx) and nonsep_idx[r - 1] == nonsep_idx[r] - 1:
            r += 1
        res.append((nonsep_idx[l + 1], nonsep_idx[r - 1] + 1))
    
    return res

# take only angklung lines
# remove first entry containing ANGKLUNG_SIGN
def get_angklung_lines(input):
    return reduce(lambda x,y : x + [y], [input[i][1:] for grp in akl_idx for i in range(grp[0], grp[1])], [])


a = flatten(f.body[1])
akl_idx = find_angklung_index(a)

b = get_angklung_lines(a)
print(flip_axes(b))
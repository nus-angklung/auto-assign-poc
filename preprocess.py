#! /usr/bin/env python3

# This file contain utilities to preprocess files before we are ready.
# Output is expected to be a list of sets, where the sets represents all notes played in a crotchet

from functools import reduce
from parse import parse, parse_token_get_last

ANGKLUNG_SIGN = 'Ang.'
akl_idx = []

# assumption: all instruments have same length, otherwise will take shortest length
# l is a 2D nested list
def flip_axes(l):
    return [list(col) for col in zip(*l)]

def flatten(input):
    return [
        reduce(lambda x, y: x + y, row, []) 
        for row in input
    ]

# which lines belong to angklung?
# Expect input to be a 2D list
# each lines is represented as a tuple of indexes (left, right)
# where left idx inclusive, right idx exclusive
def find_angklung_index(input):
    # index of non-separator lines
    nonsep_idx = [i for i, row in enumerate(input) if ''.join(row) != '']
    angklung_idx = [i for i, row in enumerate(input) if row[0] == ANGKLUNG_SIGN]

    res = []
    for i in angklung_idx:
        start = nonsep_idx.index(i)
        # finding continuous range of indexes containing start
        l, r = start - 1, start + 1
        while l >= 0 and nonsep_idx[l + 1] == nonsep_idx[l] + 1:
            l -= 1
        while r < len(nonsep_idx) and nonsep_idx[r - 1] == nonsep_idx[r] - 1:
            r += 1
        res.append((nonsep_idx[l + 1], nonsep_idx[r - 1] + 1))
    
    return res

# Expect input to be a 2D list. Return only angklung rows
def get_angklung_lines(input, akl_idx, remove_first = False) -> list:
    res = []
    for grp in akl_idx:
        for i in range(*grp):
            if i >= len(input):
                return []
            res += [input[i][1:] if remove_first else input[i]]
    return res
    
# Expect a 3D nested list f
# Substitute dots for previous note
def subs_dots(f):
    ctx = []
    for i in range(len(f)): # section
        for j in range(len(f[i])): # row
            for k in range(len(f[i][j])): # note
                f[i][j][k] = f[i][j][k].strip()

                # update current . with previous ctx
                if f[i][j][k] == ".":
                    f[i][j][k] = ctx[j]
                
                # update ctx
                last_note = parse_token_get_last(f[i][j][k])
                if j >= len(ctx):
                    ctx.append(last_note)
                else:
                    ctx[j] = last_note
    return

# Expects f to be a 3D nested list
# Returns a processed 3D nested list with no non-notes lines
def clean(f):
    # flatten the file, ignore first because it's title
    a = [flatten(x) for x in f.body[1:]]
    # filter non notes lines
    a = list(filter(lambda x: len(x) > 2, a))
    # substitute dots with previous notes
    subs_dots(a)
    return a

# Expects f to be a 3D nested list
# Return a list of sets
def transform(f):
    # process first line because it might contain the ANGKLUNG_SIGN
    akl_idx = find_angklung_index(f[0])
    res = [parse(x) for x in flip_axes(get_angklung_lines(f[0], akl_idx, True))]
    for b in f[1:]:
        b = get_angklung_lines(b, akl_idx)
        b = flip_axes(b)
        b = [parse(c) for c in b]
        res += b
    return res

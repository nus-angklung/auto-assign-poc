#! /usr/bin/env python3

# This file contains the pattern for interpreting symbols in our music sheet
# Different fonts might need different regexes
import re
from functools import reduce

p = r"[1-7][\\/]?[<>]?"

def parse(col) -> set:
    return reduce(
        lambda x, y: x.union(_parse_token(y)),
        col,
        set()
    )
    
def _parse_token(s: str) -> set:
    return set(re.findall(p, str(s)))

def parse_token_get_last(s: str) -> set:
    a = re.findall(p, str(s)) 
    return a[-1] if len(a) > 0 else s

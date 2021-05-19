# The logic to assign angklung goes here

# Expects input to be a list of sets
def gen_assignment(input):
    pass

# encode the problem as a job scheduling problem
def _encode(input):
    pass

# Generate which notes cannot be played together
# Expects input to be a list of sets
# Outputs a dictionary, with key = note, value: how many notes it plays + a list of non-conflicting notes
def gen_nonconflict_report(input):
    conflicts = {} # set of all conflicts 
    stats = {}  
    for i in range(len(input)):
        for j in input[i]:
            if j not in stats:
                stats[j] = 1
            else:
                stats[j] += 1
            
            if j not in conflicts:
                conflicts[j] = set()
            if i != 0:
                conflicts[j] |= input[i - 1]
            if i != len(input) - 1:
                conflicts[j] |= input[i + 1]
            conflicts[j] |= input[i]
    
    keys = conflicts.keys()
    nonconflicts = {k : list(keys - v) for k, v in conflicts.items()}
    return nonconflicts, stats

class Stats:
    def __init__(self):
        self.non_conflict = set()
        self.n = 0

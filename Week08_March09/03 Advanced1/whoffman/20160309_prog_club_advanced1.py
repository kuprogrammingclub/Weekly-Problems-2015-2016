import pdb
import re
import itertools
from collections import OrderedDict


# Creates a memoization table to store all substrings
def commonSub(x, y):
    l = [[0 for x in range(len(x))] for y in range(len(y))]
    z = 5
    ret = list()
    for i in range(len(y)):
        for j in range(len(x)):
            if x[j] == y[i]:
                if i == 0 or j == 0:
                    l[i][j] = 1
                else:
                    l[i][j] = l[i - 1][j - 1] + 1
                if l[i][j] >= z:
                    z = l[i][j]
                    ret.append(y[i - z + 1:i + 1])
                    z = 5
            else:
                l[i][j] = 0
    return ret

# Imports all sayings, normalizes them, and creates a list of all possible comparisons
sayings = list()
f = open('adv1.txt', 'r')
for line in f:
    sayings.append(re.sub("[^a-zA-Z]", "", line).lower())
saying_pairs = list(itertools.combinations(sayings, 2))

# Creates an ordered dictionary of common substrings (key) and the sayings that share the substring (value)
substring_dict = {}
for p1, p2 in saying_pairs:
    temp = commonSub(p1, p2)
    for i in temp:
        if i not in substring_dict:
            substring_dict[i] = [p1, p2]
        else:
            substring_dict[i] += [p2]
substring_dict = OrderedDict(sorted(substring_dict.items(),
                                    key=lambda x: len(x[1]),
                                    reverse=True))

# Solves for optimal (least common substrings)
marked = list()
common = set()
for i, k in substring_dict.items():
    for j in k:
        if j not in marked:
            marked.append(j)
            common.add(i)
    if len(marked) == len(sayings):
        print(common)
        exit(1)
if len(marked) != len(sayings):
    print("Could not find a solution")
    exit(0)

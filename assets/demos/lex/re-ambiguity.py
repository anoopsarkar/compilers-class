import nltk, string
from nltk import CFG
import sys

grammar = CFG.fromstring("""
R -> R '|' R | R R | R '*' | 'a' | 'b' | 'c'
""")

if len(sys.argv) == 1:
    inp = 'a c | b c'
else:
    for line in sys.stdin:
        inp = line.strip()
inp = inp.translate(str.maketrans('', '', string.whitespace))
print(inp)
print("Start:", grammar.start(), file=sys.stderr)
print("Productions:", grammar.productions(), file=sys.stderr)
parser = nltk.ChartParser(grammar)
for i, tree in enumerate(parser.parse([c for c in inp]), 1):
    print(i, tree)

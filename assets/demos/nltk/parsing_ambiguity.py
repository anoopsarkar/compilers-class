import nltk
from nltk import CFG
from nltk.draw.tree import draw_trees
import sys

grammar = CFG.fromstring("""
X -> X X | 'a' | 'b' | 'c' | 'd'
""")

print("Start:", grammar.start(), file=sys.stderr)
print("Productions:", grammar.productions(), file=sys.stderr)
for line in sys.stdin:
    text = line.strip().split()
    parser = nltk.ChartParser(grammar)
    for tree in parser.parse(text):
        print(tree)
    trees = parser.parse(text)
    draw_trees(*trees)

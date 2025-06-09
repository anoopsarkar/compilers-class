import sys
import nltk, string
import draw
from nltk import CFG

grammar = CFG.fromstring("""
E -> E '-' E | E '/' E | '(' E ')' | ID
ID -> 'a' | 'b' | 'c'
""")

inp = 'a - b / c'
print(inp)
print("Start:", grammar.start(), file=sys.stderr)
print("Productions:", grammar.productions(), file=sys.stderr)
parser = nltk.ChartParser(grammar)
trees = []
for i, tree in enumerate(parser.parse(inp.split()), 1):
    print(i, tree)
    trees.append(tree)
draw.draw(trees, "CFG ambiguity")

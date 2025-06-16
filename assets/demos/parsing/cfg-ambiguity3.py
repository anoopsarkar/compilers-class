import sys
import nltk
import draw

grammar = nltk.CFG.fromstring("""
E -> E '-' T
E -> T
T -> T '/' F
T -> F
F -> ID
F -> '(' E ')'
ID -> 'a' | 'b' | 'c'
""")

inp = 'a - b - c'
print(inp)
print("Start:", grammar.start(), file=sys.stderr)
print("Productions:", grammar.productions(), file=sys.stderr)
parser = nltk.ChartParser(grammar)
trees = []
for i, tree in enumerate(parser.parse(inp.split()), 1):
    print(i, tree)
    trees.append(tree)
draw.draw(trees, "CFG ambiguity")

#inp = 'a - b / c'
#print(inp)
#print("Start:", grammar.start(), file=sys.stderr)
#print("Productions:", grammar.productions(), file=sys.stderr)
#parser = nltk.ChartParser(grammar)
#for i, tree in enumerate(parser.parse(inp.split()), 1):
#    print(i, tree)
#    trees.append(tree)
#
#inp = '( a - b ) / c'
#print(inp)
#print("Start:", grammar.start(), file=sys.stderr)
#print("Productions:", grammar.productions(), file=sys.stderr)
#parser = nltk.ChartParser(grammar)
#for i, tree in enumerate(parser.parse(inp.split()), 1):
#    print(i, tree)
#    trees.append(tree)
#
#draw.draw(trees, "CFG ambiguity")

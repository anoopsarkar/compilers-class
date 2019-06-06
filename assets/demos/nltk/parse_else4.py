import nltk
from nltk import CFG
from nltk.draw.tree import draw_trees
import sys

if_grammar = """
    STMT -> IF EXPR THEN STMT
    STMT -> MATCHED_STMT
    MATCHED_STMT -> IF EXPR THEN MATCHED_STMT ELSE STMT
    MATCHED_STMT -> 'other'
    IF -> 'if'
    EXPR -> 'expr'
    THEN -> 'then'
    ELSE -> 'else'
"""
grammar = CFG.fromstring(if_grammar)
text = "if expr then if expr then other else if expr then other else other".split()
print("Start:", grammar.start(), file=sys.stderr)
print("Productions:", grammar.productions(), file=sys.stderr)
parser = nltk.ChartParser(grammar)
trees = parser.parse(text)
for tree in trees:
    print(tree)
trees = parser.parse(text)
draw_trees(*trees)

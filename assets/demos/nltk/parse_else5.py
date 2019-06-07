import nltk
from nltk import CFG
from nltk.draw.tree import draw_trees
import sys

from nltk import CFG
if_grammar = """
    STMT -> MATCHED_STMT
    STMT -> UNMATCHED_STMT
    MATCHED_STMT -> IF EXPR THEN MATCHED_STMT ELSE MATCHED_STMT
    MATCHED_STMT -> 'other'
    UNMATCHED_STMT -> IF EXPR THEN STMT
    UNMATCHED_STMT -> IF EXPR THEN MATCHED_STMT ELSE UNMATCHED_STMT
    IF -> 'if'
    EXPR -> 'expr'
    THEN -> 'then'
    ELSE -> 'else'
"""
grammar = CFG.fromstring(if_grammar)
for prod in grammar.productions():
    print(prod)
text = "if expr then if expr then other else if expr then other else other".split()
#print("Start:", grammar.start(), file=sys.stderr)
#print("Productions:", grammar.productions(), file=sys.stderr)
parser = nltk.ChartParser(grammar)
trees = parser.parse(text)
for tree in trees:
    print(tree)
trees = parser.parse(text)
draw_trees(*trees)

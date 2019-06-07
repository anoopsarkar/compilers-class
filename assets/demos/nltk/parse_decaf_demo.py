import nltk
from nltk import CFG
from nltk.draw.tree import draw_trees
import sys

decaf_func_grammar = """
    F -> 'func' ID '(' PARAMS ')' TYPE '{' BODY '}'
    ID -> 'a' | 'b' | 'c' | 'd'
    PARAMS -> HAS_PARAMS | 
    HAS_PARAMS -> ID TYPE ',' HAS_PARAMS | ID TYPE
    TYPE -> 'int' | 'char'
    BODY -> 'return' '(' ID ')' ';'
"""
grammar = CFG.fromstring(decaf_func_grammar)
text = "func a ( b int , c int , d int ) int { return ( c ) ; }".split()
parser = nltk.ChartParser(grammar)
trees = parser.parse(text)
for tree in trees:
    print(tree)
trees = parser.parse(text)
draw_trees(*trees)

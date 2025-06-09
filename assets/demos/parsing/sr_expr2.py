import nltk
from srgui import InteractiveShiftReduceGUI

grammar = nltk.CFG.fromstring("""
    E -> E PLUS T
    E -> T
    T -> T TIMES F
    T -> F
    F -> LPAREN E RPAREN
    F -> ID
    PLUS -> '+'
    TIMES -> '*'
    LPAREN -> '('
    RPAREN -> ')'
    ID -> 'a'
    ID -> 'b'
    ID -> 'c'
    """)

for prod in grammar.productions():
    print(prod)

sent = 'a * b + c'.split()
app = InteractiveShiftReduceGUI(grammar, sent)
app.mainloop()

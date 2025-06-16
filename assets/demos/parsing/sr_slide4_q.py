import nltk
from srgui import InteractiveShiftReduceGUI

grammar = nltk.CFG.fromstring("""
    E -> T PLUS E
    E -> T
    T -> ID
    T -> ID TIMES T
    T -> LPAREN E RPAREN
    PLUS -> '+'
    TIMES -> '*'
    LPAREN -> '('
    RPAREN -> ')'
    ID -> 'id'
    ID -> 'a'
    ID -> 'b'
    ID -> 'c'
    """)

for prod in grammar.productions():
    print(prod)

sent = 'id * ( id * id )'.split()
app = InteractiveShiftReduceGUI(grammar, sent)
app.mainloop()

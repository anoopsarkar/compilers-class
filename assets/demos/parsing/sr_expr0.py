import nltk
from srgui import InteractiveShiftReduceGUI

grammar = nltk.CFG.fromstring("""
    E -> E PLUS E
    E -> E TIMES E
    E -> MINUS E
    E -> LPAREN E RPAREN
    E -> ID
    PLUS -> '+'
    TIMES -> '*'
    MINUS -> '-'
    LPAREN -> '('
    RPAREN -> ')'
    ID -> 'a'
    ID -> 'b'
    ID -> 'c'
    """)

for prod in grammar.productions():
    print(prod)

sent = '- ( a + b )'.split()
app = InteractiveShiftReduceGUI(grammar, sent)
app.mainloop()

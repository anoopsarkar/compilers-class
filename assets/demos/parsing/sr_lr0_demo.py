import nltk
from srgui import InteractiveShiftReduceGUI

grammar = nltk.CFG.fromstring("""
    T -> F
    T -> T '*' F
    F -> 'id'
    F -> '(' T ')'
    """)

for prod in grammar.productions():
    print(prod)

sent = '( id ) * id'.split()
app = InteractiveShiftReduceGUI(grammar, sent)
app.mainloop()

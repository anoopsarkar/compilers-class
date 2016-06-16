import matplotlib
matplotlib.use("TkAgg")
import nltk

grammar = nltk.CFG.fromstring("""
    E -> E PLUS T
    E -> T
    T -> T TIMES F
    T -> F
    F -> ID
    PLUS -> '+'
    TIMES -> '*'
    ID -> 'a'
    ID -> 'b'
    ID -> 'c'
    """)

for prod in grammar.productions():
    print(prod)

sent = 'a + b * c'.split()
nltk.app.rdparser_app.RecursiveDescentApp(grammar, sent).mainloop()


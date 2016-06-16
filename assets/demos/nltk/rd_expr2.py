import matplotlib
matplotlib.use("TkAgg")
import nltk

grammar = nltk.CFG.fromstring("""
    E -> T E1
    E1 -> PLUS T E1
    E1 ->
    T -> F T1
    T1 -> TIMES F T1
    T1 -> 
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


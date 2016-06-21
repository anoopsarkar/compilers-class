import matplotlib
matplotlib.use("TkAgg")
import nltk

grammar = nltk.CFG.fromstring("""
    T -> F
    T -> T '*' F
    F -> 'id'
    F -> '(' T ')'
    """)

for prod in grammar.productions():
    print(prod)

sent = '( id ) * id'.split()
nltk.app.srparser_app.ShiftReduceApp(grammar, sent).mainloop()


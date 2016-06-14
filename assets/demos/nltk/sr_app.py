import matplotlib
matplotlib.use("TkAgg")
import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    NP -> 'I'
    N -> 'man' | 'park' | 'telescope' | 'dog'
    Det -> 'the' | 'a'
    P -> 'in' | 'with'
    V -> 'saw'
    """)

for prod in grammar.productions():
    print(prod)

sent = 'I saw a man in the park'.split()
nltk.app.srparser_app.ShiftReduceApp(grammar, sent).mainloop()


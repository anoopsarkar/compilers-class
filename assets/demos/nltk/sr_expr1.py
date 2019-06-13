import nltk

grammar = nltk.CFG.fromstring("""
    T -> F
    T -> T TIMES F
    F -> LPAREN T RPAREN
    F -> ID
    TIMES -> '*'
    LPAREN -> '('
    RPAREN -> ')'
    ID -> 'a'
    ID -> 'b'
    ID -> 'c'
    """)

for prod in grammar.productions():
    print(prod)

sent = '( a ) * b'.split()
nltk.app.srparser_app.ShiftReduceApp(grammar, sent).mainloop()


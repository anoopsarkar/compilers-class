import nltk

grammar = nltk.CFG.fromstring("""
    E -> T E1
    E1 -> PLUS T E1
    E1 -> 
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

sent = 'a + b'.split()
nltk.app.srparser_app.ShiftReduceApp(grammar, sent).mainloop()


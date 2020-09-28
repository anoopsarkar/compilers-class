import nltk

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

sent = 'a + b * c'.split()
nltk.app.srparser_app.ShiftReduceApp(grammar, sent).mainloop()


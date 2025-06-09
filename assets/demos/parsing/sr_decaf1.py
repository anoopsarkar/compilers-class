import nltk
from srgui import InteractiveShiftReduceGUI

grammar = nltk.CFG.fromstring("""
    F -> 'func' ID '(' PARAMS ')' TYPE '{' BODY '}'
    ID -> 'a' | 'b' | 'c'
    PARAMS -> HAS_PARAMS | 
    HAS_PARAMS -> ID TYPE ',' HAS_PARAMS | ID TYPE
    TYPE -> 'int' | 'char'
    BODY -> 'return' '(' ID ')' ';'
    """)

for prod in grammar.productions():
    print(prod)

text = """
    func a ( b int , c int ) int { return ( b ) ; }
""".split()
app = InteractiveShiftReduceGUI(grammar, text)
app.mainloop()


from rdparser_app import RecursiveDescentApp

def if_then_else_demo():
    """
    Demo if-then-else grammar
    """
    from nltk.grammar import Nonterminal, Production, ContextFreeGrammar
    nonterminals = 'E PLUS T TIMES F LPAREN RPAREN ID'
    (E, PLUS, T, TIMES, F, LPAREN, RPAREN, ID) = [Nonterminal(s) for s in nonterminals.split()]
    productions = (
        Production(E, [E, PLUS, T]),
        Production(E, [T]),
        Production(T, [T, TIMES, F]),
        Production(T, [F]),
        Production(F, [LPAREN, E, RPAREN]),
        Production(F, [ID]),

        Production(PLUS, ['+']),
        Production(TIMES, ['*']),
        Production(LPAREN, ['(']),
        Production(RPAREN, [')']),
        Production(ID, ['a']),
        Production(ID, ['b']),
        Production(ID, ['c']),
        )
    grammar = ContextFreeGrammar(E, productions)
    text = "a * b + c".split()
    RecursiveDescentApp(grammar, text).mainloop()
    
if __name__ == '__main__': if_then_else_demo()


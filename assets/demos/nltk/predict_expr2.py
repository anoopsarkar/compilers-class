
from rdparser_app import RecursiveDescentApp

def if_then_else_demo():
    """
    Demo if-then-else grammar
    """
    from nltk.grammar import Nonterminal, Production, ContextFreeGrammar
    nonterminals = 'E E1 PLUS T T1 TIMES F LPAREN RPAREN ID'
    (E, E1, PLUS, T, T1, TIMES, F, LPAREN, RPAREN, ID) = [Nonterminal(s) for s in nonterminals.split()]
    productions = (
        Production(E, [T, E1]),
        Production(E1, [PLUS, T, E1]),
        Production(E1, []),
        Production(T, [F, T1]),
        Production(T1, [TIMES, F, T1]),
        Production(T1, []),
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


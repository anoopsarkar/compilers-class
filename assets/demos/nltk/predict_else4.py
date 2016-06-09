
from rdparser_app import RecursiveDescentApp

def if_then_else_demo():
    """
    Demo if-then-else grammar
    """
    from nltk.grammar import Nonterminal, Production, ContextFreeGrammar
    nonterminals = 'STMT MATCHED_STMT IF EXPR THEN ELSE'
    (STMT, MATCHED_STMT, IF, EXPR, THEN, ELSE) = [Nonterminal(s) for s in nonterminals.split()]
    productions = (
        Production(STMT, [ IF, EXPR, THEN, STMT ]),
        Production(STMT, [ MATCHED_STMT ]),

        Production(MATCHED_STMT, [ IF, EXPR, THEN, MATCHED_STMT, ELSE, STMT ]),

        Production(IF, ['if']),
        Production(EXPR, ['expr']),
        Production(THEN, ['then']),
        Production(MATCHED_STMT, ['other']),
        Production(ELSE, ['else']),
        )
    grammar = ContextFreeGrammar(STMT, productions)

    text = "if expr then if expr then other else if expr then other else other".split()

    RecursiveDescentApp(grammar, text).mainloop()

    
if __name__ == '__main__': if_then_else_demo()


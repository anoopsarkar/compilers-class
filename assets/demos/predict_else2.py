
from rdparser_app import RecursiveDescentApp

def if_then_else_demo():
    """
    Demo if-then-else grammar
    """
    from nltk.grammar import Nonterminal, Production, ContextFreeGrammar
    nonterminals = 'STMT IF EXPR THEN ELSE OPTELSE'
    (STMT, IF, EXPR, THEN, ELSE, OPTELSE) = [Nonterminal(s) for s in nonterminals.split()]
    productions = (
        Production(STMT, [IF, EXPR, THEN, STMT, OPTELSE]),
        Production(OPTELSE, [ELSE, STMT]),
        Production(OPTELSE, []),

        Production(IF, ['if']),
        Production(EXPR, ['expr']),
        Production(THEN, ['then']),
        Production(STMT, ['other']),
        Production(ELSE, ['else']),
        )
    grammar = ContextFreeGrammar(STMT, productions)

    text = "if expr then if expr then other else other".split()

    RecursiveDescentApp(grammar, text).mainloop()

    
if __name__ == '__main__': if_then_else_demo()


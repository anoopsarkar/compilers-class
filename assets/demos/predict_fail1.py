
from rdparser_app import RecursiveDescentApp

def fail_demo():
    """
    Demo grammar that should not work with backtracking for all inputs
    """
    from nltk.grammar import Nonterminal, Production, ContextFreeGrammar
    S = Nonterminal('S')
    A = Nonterminal('A')
    productions = (
        Production(S, [ A, S, A ]),
        Production(S, [ A, A ]),
        Production(A, [ 'a' ]),
        )
    grammar = ContextFreeGrammar(S, productions)

    text = "a a a a a a".split()
    #text = "a a a a".split()

    RecursiveDescentApp(grammar, text).mainloop()

if __name__ == '__main__': fail_demo()



from nltk import tokenize 
from srparser_app import ShiftReduceApp

def app():
    """
    Create a shift reduce parser app, using a simple grammar and
    text. 
    """
    
    from nltk.grammar import Nonterminal, Production, ContextFreeGrammar
    nonterminals = 'E E1 PLUS T T1 TIMES F LPAREN RPAREN ID'
    (E, E1, PLUS, T, T1, TIMES, F, LPAREN, RPAREN, ID) = [Nonterminal(s) for s in nonterminals.split()]
    productions = ( 
        Production(E, [T, E1]),
        Production(E1, [PLUS, T, E1]),
        Production(E1, []),
        Production(T, [F]),
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

    # tokenize the sentence
    text = "a + b".split()

    ShiftReduceApp(grammar, text).mainloop()

if __name__ == '__main__':
    app()

__all__ = ['app']


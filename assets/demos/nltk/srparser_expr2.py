
from nltk import tokenize 
from srparser_app import ShiftReduceApp

def app():
    """
    Create a shift reduce parser app, using a simple grammar and
    text. 
    """
    
    from nltk.grammar import Nonterminal, Production, ContextFreeGrammar
    nonterminals = 'T F'
    (T, F) = [Nonterminal(s) for s in nonterminals.split()]
    
    productions = (
    Production(T, [F]),
    Production(T, [T, '*', F]),
    Production(F, ['id']),
    Production(F, ['(', T, ')']),
    )

    grammar = ContextFreeGrammar(T, productions)

    # tokenize the sentence
    text = "( id ) * id".split()

    ShiftReduceApp(grammar, text).mainloop()

if __name__ == '__main__':
    app()

__all__ = ['app']


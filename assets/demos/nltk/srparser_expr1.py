
from nltk import tokenize 
from srparser_app import ShiftReduceApp

def app():
    """
    Create a shift reduce parser app, using a simple grammar and
    text. 
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

    # tokenize the sentence
    text = "a * b + c".split()

    ShiftReduceApp(grammar, text).mainloop()

if __name__ == '__main__':
    app()

__all__ = ['app']


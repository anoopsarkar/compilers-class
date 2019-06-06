
from nltk.app.srparser_app import ShiftReduceApp

def app():
    """
    Create a shift reduce parser app, using a simple grammar and
    text. 
    """
    from nltk import CFG
    expr_grammar = """
        E -> E PLUS T
        E -> T
        T -> T TIMES F
        T -> F
        F -> LPAREN E RPAREN
        F -> ID

        PLUS -> '+'
        TIMES -> '*'
        LPAREN -> '('
        RPAREN -> ')'
        ID -> 'a'
        ID -> 'b'
        ID -> 'c'
    """
    grammar = CFG.fromstring(expr_grammar)
    text = "a * b + c".split()
    ShiftReduceApp(grammar, text).mainloop()

if __name__ == '__main__':
    app()

__all__ = ['app']


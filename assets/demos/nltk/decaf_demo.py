
from nltk.app.rdparser_app import RecursiveDescentApp

def demo():
    """
    Demo decaf grammar
    """
    from nltk import CFG
    decaf_func_grammar = """
        F -> 'func' ID '(' PARAMS ')' TYPE '{' BODY '}'
        ID -> 'a' | 'b' | 'c'
        PARAMS -> HAS_PARAMS | 
        HAS_PARAMS -> ID TYPE ',' HAS_PARAMS | ID TYPE
        TYPE -> 'int' | 'char'
        BODY -> 'return' '(' ID ')' ';'
    """
    grammar = CFG.fromstring(decaf_func_grammar)
    text = """
        func a ( b int , c int ) int { return ( b ) ; }
    """.split()
    RecursiveDescentApp(grammar, text).mainloop()
    
if __name__ == '__main__': demo()


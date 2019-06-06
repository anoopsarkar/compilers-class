
from nltk.app.rdparser_app import RecursiveDescentApp

def if_then_else_demo():
    """
    Demo if-then-else grammar
    """
    from nltk import CFG
    if_grammar = """
        STMT -> IF EXPR THEN STMT
        STMT -> MATCHED_STMT
        MATCHED_STMT -> IF EXPR THEN MATCHED_STMT ELSE STMT
        MATCHED_STMT -> 'other'
        IF -> 'if'
        EXPR -> 'expr'
        THEN -> 'then'
        ELSE -> 'else'
    """
    grammar = CFG.fromstring(if_grammar)
    text = "if expr then if expr then other else if expr then other else other".split()
    RecursiveDescentApp(grammar, text).mainloop()

    
if __name__ == '__main__': if_then_else_demo()



from nltk.app.rdparser_app import RecursiveDescentApp

def if_then_else_demo():
    """
    Demo if-then-else grammar
    """
    from nltk import CFG
    if_grammar = """
        STMT -> MATCHED_STMT
        STMT -> UNMATCHED_STMT
        MATCHED_STMT -> IF EXPR THEN MATCHED_STMT ELSE MATCHED_STMT
        MATCHED_STMT -> 'other'
        UNMATCHED_STMT -> IF EXPR THEN STMT
        UNMATCHED_STMT -> IF EXPR THEN MATCHED_STMT ELSE UNMATCHED_STMT
        IF -> 'if'
        EXPR -> 'expr'
        THEN -> 'then'
        ELSE -> 'else'
    """
    grammar = CFG.fromstring(if_grammar)
    text = "if expr then if expr then other else if expr then other else other else other".split()
    RecursiveDescentApp(grammar, text).mainloop()
    
if __name__ == '__main__': if_then_else_demo()


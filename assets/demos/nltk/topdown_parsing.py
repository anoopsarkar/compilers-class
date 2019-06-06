
from nltk.app.rdparser_app import RecursiveDescentApp

def if_then_else_demo():
    """
    Demo if-then-else grammar
    """
    from nltk import CFG
    if_grammar = """
        # Grammatical productions.
        S -> NP VP
        NP -> Det N PP | Det N
        VP -> V NP PP | V NP | V
        PP -> P NP

        # Lexical productions.
        NP -> 'I'
        Det -> 'the' | 'a'
        N -> 'man' | 'park' | 'dog' | 'telescope'
        V -> 'ate' | 'saw'
        P -> 'in' | 'under' | 'with'
    """
    grammar = CFG.fromstring(if_grammar)
    text = 'the dog saw a man in the park'.split()
    RecursiveDescentApp(grammar, text).mainloop()
    
if __name__ == '__main__': if_then_else_demo()


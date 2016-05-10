
from nltk.draw.rdparser import RecursiveDescentDemo

def regexp():
    """
    Demo regexp grammar
    """
    from nltk.parse import cfg
    nonterminals = 'R OR STAR LPAREN RPAREN A B'
    (R, OR, STAR, LPAREN, RPAREN, A, B) = [cfg.Nonterminal(s) for s in nonterminals.split()]
    productions = (
        cfg.Production(R, [R, OR, R]),
        cfg.Production(R, [R, R]),
        cfg.Production(R, [R, STAR]),
        cfg.Production(R, [LPAREN, R, RPAREN]),
        cfg.Production(R, [A]),
        cfg.Production(R, [B]),

        cfg.Production(OR, ['|']),
        cfg.Production(STAR, ['*']),
        cfg.Production(LPAREN, ['(']),
        cfg.Production(RPAREN, [')']),
        cfg.Production(A, ['a']),
        cfg.Production(B, ['b']),
        )
    grammar = cfg.Grammar(R, productions)

    text = "a | b * a".split()

    RecursiveDescentDemo(grammar, text).mainloop()

    
if __name__ == '__main__': regexp()


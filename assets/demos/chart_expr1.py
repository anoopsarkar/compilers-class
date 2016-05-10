
from nltk.draw.chart import ChartDemo

def expr_chart_demo():
    """
    Demo expression grammar
    """
    from nltk.parse import cfg
    nonterminals = 'E PLUS T TIMES F LPAREN RPAREN ID'
    (E, PLUS, T, TIMES, F, LPAREN, RPAREN, ID) = [cfg.Nonterminal(s) for s in nonterminals.split()]
    productions = (
        cfg.Production(E, [E, PLUS, T]),
        cfg.Production(E, [T]),
        cfg.Production(T, [T, TIMES, F]),
        cfg.Production(T, [F]),
        cfg.Production(F, [LPAREN, E, RPAREN]),
        cfg.Production(F, [ID]),

        cfg.Production(PLUS, ['+']),
        cfg.Production(TIMES, ['*']),
        cfg.Production(LPAREN, ['(']),
        cfg.Production(RPAREN, [')']),
        cfg.Production(ID, ['a']),
        cfg.Production(ID, ['b']),
        cfg.Production(ID, ['c']),
        )
    grammar = cfg.Grammar(E, productions)

    text = "a * b + c".split()

    ChartDemo(grammar, text).mainloop()

    
if __name__ == '__main__': expr_chart_demo()


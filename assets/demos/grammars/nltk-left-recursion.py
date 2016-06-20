import nltk
from collections import defaultdict

grammar1 = nltk.CFG.fromstring("""
    S -> A 'a' | 'b'
    A -> A 'c' | S 'd' | 
    """)

output1 = nltk.CFG.fromstring("""
    S -> A 'a' | 'b'
    A -> 'b' 'd' A_r | A_r
    A_r -> 'c' A_r | 'a' 'd' A_r | 
    """)

grammar2 = nltk.CFG.fromstring("""
    S -> A 'a' | 'b'
    A -> A 'c' | S 'd' | B
    B -> B 'e' | A 'f' | S 'g' | 'h'
    """)

def ordered_lhs(g):
    lhs_set = set([r.lhs() for r in g.productions()])
    ordered_lhs = [n for n in filter(lambda x: g.start() != x, lhs_set)]
    ordered_lhs.sort()
    ordered_lhs.insert(0, g.start())
    return ordered_lhs

def new_nonterminal(n):
    nsym = n.symbol() + '_r'
    return nltk.Nonterminal(nsym)

def print_grammar(g):
    print 'start:', g.start()
    for r in g.productions():
        print 'rule:', r

def print_rules(rules, nonterminal):
    print "Current nonterminal:", nonterminal
    cur_g = nltk.CFG(nonterminal, rules, calculate_leftcorners=False)
    print cur_g


def lhs_rules(rules, lhs):
    return filter(lambda x: x.lhs() == lhs, rules)

def group_rhs(rules, lhs, match):
    matched = []
    not_matched = []
    for r in lhs_rules(rules, lhs):
        rhs = r.rhs()
        if len(r) > 0:
            first = rhs[0]
            if nltk.grammar.is_nonterminal(first) and first == match:
                matched.append(r)
            else:
                not_matched.append(r)
        else:
            not_matched.append(r)
    return matched, not_matched

def noleft_immediate(rules, lhs):
    (left, not_left) = group_rhs(rules, lhs, lhs)
    new_rules = []
    if len(left) > 0:
        new_lhs = new_nonterminal(lhs)
        for r in not_left:
            new_rules.append( nltk.Production(lhs, r.rhs() + (new_lhs,)) )
        for r in left:
            old_rhs = r.rhs()
            if len(old_rhs) > 0:
                new_rules.append( nltk.Production(new_lhs, r.rhs()[1:] + (new_lhs,)) )
            else:
                new_rules.append( nltk.Production(lhs, old_rhs) )
        new_rules.append( nltk.Production(new_lhs, ()) )
    else:
        new_rules = rules
    return new_rules

def expand_match(rules, expand_rules, lhs, match):
    (matched, not_matched) = group_rhs(expand_rules, lhs, match)
    new_rules = []
    if len(matched) > 0:
        for r in matched:
            for match_rule in lhs_rules(rules, match):
                new_rules.append( nltk.Production(lhs, match_rule.rhs() + r.rhs()[1:]) )
        new_rules.extend( not_matched )
    else:
        new_rules.extend( not_matched )
    return new_rules

def noleft(g):
    print "Before:"
    print g
    lhs_list = ordered_lhs(g)
    rules = []
    for i in range(len(lhs_list)):
        expand_rules = []
        for j in range(i):
            expand_rules.extend( expand_match(rules, g.productions(lhs_list[i]), lhs_list[i], lhs_list[j]) )
        if len(expand_rules) > 0:
            rules.extend( noleft_immediate(expand_rules, lhs_list[i]) )
        else:
            rules.extend( noleft_immediate(g.productions(lhs_list[i]), lhs_list[i]) )
    new_g = nltk.CFG(g.start(), rules, calculate_leftcorners=False)
    print "After:"
    print new_g
    
noleft(grammar1)
print output1
noleft(grammar2)

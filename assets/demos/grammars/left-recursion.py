import sys
from collections import defaultdict

G = {} # dict with context free grammar that has left recursion, key = lhs, value = rhs

#G['S'] = [ 'Aa', 'b' ]
#G['A'] = [ 'Ac', 'Sd', '' ]
# lexicographic ordering over non-terminals in G
#O = ['S', 'A']

G['S'] = [ 'Aa', 'b' ]
G['A'] = [ 'Aa', 'Sc', 'Bb' ]
G['B'] = [ 'bB', 'Aa', 'Sc' ]
# lexicographic ordering over non-terminals in G
O = ['S', 'A', 'B']

def print_grammar(G):
    for lhs in G.keys():
        for rhs in G[lhs]:
            print "{0} -> {1}".format(lhs, rhs)

def eliminate_left_recursion(G, O):
    for i in range(len(O)):
        print "before:"
        print_grammar(G)
        print "before:", O[i], "->", G[O[i]]
        for j in range(i):
            # grammar with no left recursion 
            NLR = defaultdict(list)
            rules = G[O[i]]
            for rhs in rules:
                if (rhs.find(O[j]) != -1):
                    print i, j, rhs
                    replace_rules = G[O[j]]
                    for replace_rhs in replace_rules:
                        NLR[O[i]].append(rhs.replace(O[j], replace_rhs)) 
                else:
                    NLR[O[i]].append(rhs) 
            # replace old grammar with new grammar without left recursion
            for lhs in G:
                if lhs in NLR:
                    G[lhs] = NLR[lhs]
        print "after:", O[i], "->", G[O[i]]
        G = eliminate_immediate_left_recursion(G)
    return G
    
def eliminate_immediate_left_recursion(G):
    for lhs in G.keys():
        rules = G[lhs]
        A = []
        B = []
        for rhs in rules:
            if len(rhs) > 0:
                if rhs[0] == lhs:
                    A.append(rhs)
                else:
                    B.append(rhs)
            else:
                print >>sys.stderr, "Warning: this algorithm does not always work with non-terminals that derive the empty string"
                B.append(rhs)
        G[lhs] = []
        new_lhs = lhs+"_r"
        for rhs in B:
            G[lhs].append(rhs + new_lhs)
        G[new_lhs] = []
        for rhs in A:
            G[new_lhs].append(rhs + new_lhs)
        G[new_lhs].append('') # add the empty string
    return G

if __name__ == '__main__':
    G = eliminate_left_recursion(G, O) 
    for lhs in G.keys():
        for rhs in G[lhs]:
            print "{0} -> {1}".format(lhs, rhs)

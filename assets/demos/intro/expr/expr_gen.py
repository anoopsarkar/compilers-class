import nltk
import random
import sys
from nltk import Nonterminal, PCFG
from nltk.parse.generate import generate

if len(sys.argv) < 2:
    print(f"usage: {sys.argv[0]} num")
    sys.exit(1)
num = int(sys.argv[1])

# Define a simple context-free grammar
grammar = PCFG.fromstring("""
    s -> e [1.0]
    e -> e '+' e [0.2]
    e -> e '*' e [0.2]
    e -> '(' e ')' [0.2]
    e -> n [0.4]
    n -> n n [0.02] \
      | '0' [0.098] \
      | '1' [0.098] \
      | '2' [0.098] \
      | '3' [0.098] \
      | '4' [0.098] \
      | '5' [0.098] \
      | '6' [0.098] \
      | '7' [0.098] \
      | '8' [0.098] \
      | '9' [0.098]
""")
# Set the starting symbol
start_symbol = Nonterminal('s')

# Set the seed randomly
random.seed()  # Uses system time or OS-specific randomness

# Generate and print all possible sentences up to a max depth
#print("Generated Sentences:\n")
#for sentence in generate(grammar, start=start_symbol, n=20, depth=10):
#    print(' '.join(sentence))

# Recursive function to expand a nonterminal symbol
def generate_random(symbol):
    if isinstance(symbol, str):
        return [symbol]
    productions = grammar.productions(lhs=symbol)
    probs = [prod.prob() for prod in productions]
    chosen_prod = random.choices(productions, weights=probs, k=1)[0]
    result = []
    for sym in chosen_prod.rhs():
        try:
            result.extend(generate_random(sym))
        except RecursionError:
            result.extend(['1'])
    return result

# Generate and print random sentences
for _ in range(num):  # Generate 10 random sentences
    print(''.join(generate_random(start_symbol)))

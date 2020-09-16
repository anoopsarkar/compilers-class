import re

def compile_regexps(regexps):
    regexp_dict = {}
    for (i,r) in enumerate(regexps):
        regexp_dict[i] = re.compile(r)
    return regexp_dict

def match_regexps(regexp_dict, s):
    matched_regexps = set()
    for (i,r) in regexp_dict.items():
        if regexp_dict[i].match(s):
            print("match_regexps", i, regexp_dict[i].match(s))
            matched_regexps.add(i) 
    print("match_regexps", matched_regexps)
    return matched_regexps

if __name__ == '__main__':
    import sys
    # define the regexps as strings
    regexps = [
        "^(((ac)|b)c)$",
        "^(a((c|b)c))$",
        "^(a(c|(bc)))$",
        "^((a(c|b))c)$",
        "^((ac)|(bc))$",
        "^ac|bc$"
    ]
    for (i,r) in enumerate(regexps):
        print(i, r)
    # compile each one and store in a dict
    regexp_dict = compile_regexps(regexps)
    # initialize the set of valid regexps to all of them
    valid_regexps = set(k for k in regexp_dict.keys())
    # iteratively ask for a string that can be used to disambiguate the regexps
    inputs = set()
    for s in sys.stdin:
        s = s.strip()
        inputs.add(s)
        valid_regexps = valid_regexps.intersection(match_regexps(regexp_dict, s))
        for i in valid_regexps:
            print(i, regexps[i])
    print(f"inputs: {inputs}")

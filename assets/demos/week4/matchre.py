import re
import sys
for line in sys.stdin:
    if re.match('^(ab?)*\n$', line):
        print 'yes' 
    else:
        print 'no'

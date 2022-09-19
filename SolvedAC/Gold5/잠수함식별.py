import re

string = input().strip()
p = re.compile('(100+1+|01)+')
result = p.fullmatch(string)

if result:
    print("SUBMARINE")
else:
    print("NOISE")

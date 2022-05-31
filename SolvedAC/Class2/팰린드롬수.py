result = []
while True:
    string = input()
    if string == "0":
        break
    str_reverse = string[::-1]
    if string == str_reverse:
        result.append("yes")
    else:
        result.append("no")

for r in result:
    print(r)
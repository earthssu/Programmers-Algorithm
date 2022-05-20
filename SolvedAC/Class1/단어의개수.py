string = input()
if string == '' or string == ' ':
    print(0)
else:
    print(len(string.strip(' ').split(" ")))
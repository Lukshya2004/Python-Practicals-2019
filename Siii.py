S = input()
C = input()
for i in S:
    if i == C or i == C.lower():
        i = i.upper()
    else:
        i = i.lower()

    print(i, end = "")

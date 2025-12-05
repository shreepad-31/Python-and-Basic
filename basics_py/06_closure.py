for t in range(int(input())):
    num = int(input())
    dna = input()
    n = 0
    com_dna = []
    for i in dna:
        if i == "a":
            com_dna.append("t")
        elif i == "t":
            com_dna.append("a")
        elif i == "c":
            com_dna.append("g")
        elif i == "g":
            com_dna.append("c")
    com_dna = "".join(com_dna)
    print(com_dna)
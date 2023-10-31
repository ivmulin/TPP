def CountLetters(s):
    D = dict()
    for i in s:
        if i in D.keys():
            D[i] += 1
        else:
            D[i] = 1
    return D


def Slave(s1, s2):
    D1 = CountLetters(s1)
    D2 = CountLetters(s2)
    for d in D1.keys():
        if d not in D2.keys() or D2[d] < D1[d]:
            return False
    return True


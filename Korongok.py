korongok = []
A = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
C = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
D = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
E = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
F = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
G = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
H = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
B = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',]
korongok.append(A)
korongok.append(B)
korongok.append(C)
korongok.append(D)
korongok.append(E)
korongok.append(F)
korongok.append(G)
korongok.append(H)
for lista in korongok:
    print(lista)
válasz=None
oszlop=None
while válasz != '':
    válasz = input('Írjon be egy sort 1-8 között:')
    oszlop = int(input('Írjon be egy oszlopot 1-8 között:'))
    if oszlop<1 or oszlop>8:
        print('Ilyen oszlop nem létezik!')
        continue
    match válasz:
        case '1':
            if A[oszlop-1] == 'X':
                A.pop(oszlop-1)
                A.insert(oszlop-1, 'O')
            else:
                A.pop(oszlop-1)
                A.insert(oszlop-1, 'X')
        case '2':
            if B[oszlop-1] == 'X':
                B.pop(oszlop-1)
                B.insert(oszlop-1, 'O')
            else:
                B.pop(oszlop-1)
                B.insert(oszlop-1, 'X')
        case '3':
            if C[oszlop-1] == 'X':
                C.pop(oszlop-1)
                C.insert(oszlop-1, 'O')
            else:
                C.pop(oszlop-1)
                C.insert(oszlop-1, 'X')
        case '4':
            if D[oszlop-1] == 'X':
                D.pop(oszlop-1)
                D.insert(oszlop-1, 'O')
            else:
                D.pop(oszlop-1)
                D.insert(oszlop-1, 'X')
        case '5':
            if E[oszlop-1] == 'X':
                E.pop(oszlop-1)
                E.insert(oszlop-1, 'O')
            else:
                E.pop(oszlop-1)
                E.insert(oszlop-1, 'X')
        case '6':
            if F[oszlop-1] == 'X':
                F.pop(oszlop-1)
                F.insert(oszlop-1, 'O')
            else:
                F.pop(oszlop-1)
                F.insert(oszlop-1, 'X')
        case '8':
            if H[oszlop-1] == 'X':
                H.pop(oszlop-1)
                H.insert(oszlop-1, 'O')
            else:
                H.pop(oszlop-1)
                H.insert(oszlop-1, 'X')
        case '7':
            if G[oszlop-1] == 'X':
                G.pop(oszlop-1)
                G.insert(oszlop-1, 'O')
            else:
                G.pop(oszlop-1)
                G.insert(oszlop-1, 'X')
        case other:
            print('Ilyen sor nem létezik!')
    for lista in korongok:
        print(lista)
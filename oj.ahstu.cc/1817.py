def readMatrix(row):
    A = []
    for i in xrange(row):
        A.append(list(map(int, raw_input().strip().split())))
    return A


def addMatrix(A, B):
    C = []
    for i in xrange(len(A)):
        C.append([])
        for j in xrange(len(A[i])):
            C[i].append(A[i][j] + B[i][j])
    # print C
    return C


def printMatrix(A):
    for i in xrange(len(A)):
        print str(A[i])[1:-1].replace(',', '')


row, col = map(int, raw_input().strip().split())
A = readMatrix(row)
B = readMatrix(row)
C = addMatrix(A, B)
printMatrix(C)

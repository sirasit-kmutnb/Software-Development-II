def solveEq(c1,c2,A):
    """ ใช้ในกรณีที่คำตอบใดๆ ใน set A เป็นไปได้เพียงคำตอบเดียว [Complexity : O(n^8)] """
    x1,x2,x3,x4,x5,x6,x7,x8 = 0,0,0,0,0,0,0,0
    for i in range(len(A)):
        for j in range(len(A)):
            x1 = A[i]
            x2 = A[j]
            if i == j :
                continue
            elif c1 == x1 + x2:
                # print(x1,x2)
                for k in range(len(A)):
                    for l in range(len(A)):
                        x3 = A[k]
                        x4 = A[l]
                        if k in [i,j,l] or l in [i,j]:
                            continue
                        elif x1 + x3 == x4:
                            for m in range(len(A)):
                                for n in range(len(A)):
                                    x6 = A[m]
                                    x8 = A[n]
                                    if m in [i,j,k,l,n] or n in [i,j,k,l]:
                                        continue
                                    elif x8 == c2 + x6:
                                        for o in range(len(A)):
                                            for p in range(len(A)):
                                                x5 = A[o]
                                                x7 = A[p]
                                                if o in [i,j,k,l,m,n,p] or p in [i,j,k,l,m,n]:
                                                    continue
                                                elif x7 == x5 + x6:
                                                    return x1,x2,x3,x4,x5,x6,x7,x8

def solveEqFromFile(File):
    f = open(File,'r')
    inputConstant = f.readline()
    c1 = int(inputConstant.split(" ")[1])
    c2 = int(inputConstant.split(" ")[2])
    A = []
    for i in f:
        A.append(int(i.strip()))
    A.sort()
    return solveEq(c1,c2,A)
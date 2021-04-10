
epsilon = 0.001
def dominant_Diagonal(M):
    sum=0
    count1=0
    count2=0
    for i in M:

        for j in i:
            if(count1!=count2):
                sum=sum+abs(j)
            count2 = count2 + 1
        count2=0
        if(abs(M[count1][count1])< sum):
            print("it is not dominant diagonal")
            return False

        sum=0
        count1=count1+1
    print("it is dominant diagonal")
    return True

def Jacobi_method(M,V):
    xi = 0
    yi = 0
    zi = 0
    if(True==dominant_Diagonal(M)):
        xij=xi+1
        temp=xi
        while (abs(xij-temp)>epsilon):
             xij =(V[0] - yi*M[0][1] - zi*M[0][2]) / M[0][0]
             yij = (V[1] - xi*M[1][0] - zi*M[1][2]) / M[1][1]
             zij = (V[2] - xi*M[2][0] - yi*M[2][1]) / M[2][2]
             temp=xi
             xi=xij
             yi=yij
             zi=zij
             print(xij, yij,zij )

def Gauss_Seidel_method(M,V):
    xi=0
    yi=0
    zi=0
    if(True==dominant_Diagonal(M)):
        xij=xi+1
        temp=xi
        xij = 1
        yij = 0
        zij = 0
        while (abs(xij-temp)>epsilon):
             temp = xij
             xij =(V[0] - yij*M[0][1] - zij*M[0][2]) / M[0][0]
             yij = (V[1] - xij*M[1][0] - zij*M[1][2]) / M[1][1]
             zij = (V[2] - xij*M[2][0] - yij*M[2][1]) / M[2][2]
             print(xij, yij,zij )

def main():
    M = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    V = [2, 6, 5]
    print("Gauss_Seidel_method:")
    Gauss_Seidel_method(M,V)
    print("Jacobi method:")
    Jacobi_method(M, V)
main()

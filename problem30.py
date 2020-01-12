
from problem import Problem

class Problem30(Problem):
    def __init__(self):
        
        import random

        data = []
        n=random.randint(5,7)

        for _ in range(n):
            data.append(random.randint(97,102))
        random.shuffle(data)
        
        data="".join([chr(i) for i in data])
        statement = "Primiti un sir: " + "".join([i+" " for i in data]) +". Gasiti numarul minim de "
        statement += "litere (si literele) care ar trebui introduse pentru ca sirul sa devina palindrom."
        super().__init__(statement, data)

    def solve(self):

        sir=self.data
        n=len(sir)

        dp=[[0 for i in range(n)] for i in range(n)]
        sol=[[sir[i] if i==j else "" for i in range(n)] for j in range(n)]

        solution="Idee de rezolvare: \n\n"
        solution+="Vom crea doua matrici, una care va contine numarul minim de insertii pe pozitia i,j pentru subsirul [i:j], iar cealalta care va contine palindromul creat prin numar minim de insertii pentru subsirul [i:j], pe pozitia i,j (doar deasupra diagonalei principale, matrici inferior triunghiulare)."
        solution+="\n\nMatricea cu numarul de insertii:\nParcurgem diagonalele paralele cu diagonala principala, si pentru subsirul [i:j] punem in matrice la pozitia i,j numarul minim de insertii necesar pentru a crea un palindrom."
        solution+="Luam capetele subsirului, le comparam: daca sunt egale, atunci nu avem nevoie de insertii, subsirul [i:j] are nevoie de tot atatea insertii ca subsirul [i+1:j-1]; in caz contrar, subsirul [i:j] are nevoie cu o insertie mai mult decat "
        solution+="minimul dintre numarul de insertii necesar subsirului [i:j-1], respectiv [i+1:j]. "
        solution+="\n\nMatricea cu palindroame pentru orice subsir [i:j]:\n"
        solution+="Matricea e goala la inceput, cu exceptia diagonalei principale, care contine literele din sir. Parcurgem diagonalele paralele cu "
        solution+="diagonala principala, si construim palindromul pentru subsirul [i:j], folosindu-ne de ce avem in stanga si dedesubt."

        for i in range(1,n):
            for j in range(n-i):
                left=j
                right=j+i
                if sir[left]==sir[right]:
                    dp[left][right]=dp[left+1][right-1]
                    sol[left][right]=sir[left]+sol[left+1][right-1]+sir[right]
                    
                else:
                    if dp[left+1][right]<dp[left][right-1]:
                        dp[left][right]=1+dp[left+1][right]
                        sol[left][right]=sir[left]+sol[left+1][right]+sir[left]
                    else:
                        dp[left][right]=1+dp[left][right-1]
                        sol[left][right]=sir[right]+sol[left][right-1]+sir[right]

        
        solution+="\n\n"

        for i in range(n):
            for j in range(n):
                solution+=" "*(len(sol[0][j])-len(sol[i][j]))+sol[i][j]+" "
            solution+="\n"

        solution+="\n"

        for i in range(n):
            for j in range(n):
                solution+=str(dp[i][j])+" "
            solution+="\n"

        solution+="\n\nNumarul minim de insertii este "+str(dp[0][n-1])+", iar palindromul rezultat este "+sol[0][n-1]

        return solution

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
        statement = "Primiti o lista dublu inlantuita care contine elementele: " + "".join([i+" " for i in data]) +". Gasiti numarul minim de "
        statement += "litere (si literele) care ar trebui introduse pentru ca lista sa devina palindromica."
        super().__init__(statement, data)

    def solve(self):

        sir=self.data
        n=len(sir)

        dp=[[0 for i in range(n)] for i in range(n)]
        sol=[[sir[i] if i==j else "" for i in range(n)] for j in range(n)]

        solution="Idee de rezolvare: \nVom crea doua matrici, una in care vom calcula numarul minim de insertii, "
        solution+="folosind recurenta: \n\n"
        solution+="dp[i][j]=  dp[i+1][j-1], daca sir[i]==sir[j]\n"
        solution+="           1+min(dp[i+1][j],dp[i][j-1]), daca sir[i]!=sir[j]\n"
        solution+="iar cealalta, in care vom construi treptat palindromul, dupa regula:\n\n"
        solution+="sol[i][j]=  sir[i]+sol[i+1][j-1]+sir[j], daca sir[i]==sir[j]\n"
        solution+="            sir[i]+sol[i+1][j]+sir[i], daca sir[i]!=sir[j] si dp[i+1][j]<dp[i][j-1]\n"
        solution+="            sir[j]+sol[i][j-1]+sir[j], daca sir[i]!=sir[j] si dp[i+1][j]>=dp[i][j-1]\n\n"
        solution+="La final, in ambele matrici, in coltul din dreapta sus, vom avea rezultatele: in dp vom avea numarul "
        solution+="minim de insertii, iar in sol vom avea palindromul care rezulta in urma acestor insertii "
        solution+="(palindromul nu este unic, se poate schimba inversand conditiile din ultimele 2 ramuri de la construirea matricii sol)"

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
                


        solution+="\n\nNumarul minim de insertii este "+str(dp[0][n-1])+", iar palindromul rezultat este "+sol[0][n-1]

        return solution
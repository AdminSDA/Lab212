# Lab212

## Afisare graf cu matplotlib si networkx

* Adaugati un atribut nou in clasa: **ImgName**
  * atributul trebuie declarat in init();
  * ex: *self.ImgName = ['Graf.png']*
* La salvarea figurii: *plt.savefig(self.ImgName[0])*
* Daca vreti sa aveti imaginile in cerinta(statement), adaugati un atribut **statementPicture**, care reprezinta numarul de imagini pe care le vreti in statement;
  * i.e.: primele *statementPicture* for fi puse in statement celelalte in solution.
  * daca aveti o singura imagine si o vreti in statement: *ImgName = ['numele imaginii'], statementPicture = 1*
* Se pot pune mai multe imagini  
### Imaginele trebuie generate in solve() sau alte functi apelate in solve(), nu in init()

from problem import Problem
import random 
import pickle
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def randPonds(nr):
        # generate some random frequecy for huffman
        v = [0 for i in range(0,nr)];
        N = 100;
        N += N%nr;
        for i in range(0,len(v)):
            v[i] = N//nr;
        v[0]-=N%nr;
        #acum suma lor este 100;
        for i in range(len(v)-1,0,-1):
            d = random.randint(1,v[i]//2);
            v[i]-=d;
            v[i-1]+=d;
            while(v.count(v[i]) != 1):
                v[i]-=1;
                v[i-1]+=1;
        return v;

class Problem37(Problem):
    
    def __init__(self):
        #sa citesca cuvintele si sa genereze un imput
        # data=[];
        self.solution = "";
        # se va alege un camp din heap-ul stocat
        fIn = open("Hash4.b","rb");
        dict = pickle.load(fIn)
        # ponderi = [('a',28),('r',14),('d',12),('e',20),('n',11),('t',15)];
        # ~ list = ['a','r','d','e','n','t'];
        Char = random.choice(list(dict.keys()));    # character as the key
        listChar = list(Char)                      # character as a list
        ponds = randPonds(len(listChar));
        ponderi = [(listChar[i],ponds[i]) for i in range(0,len(listChar))];
        self.makeHuffman(ponderi);
        #self.afisareHuffman(self.huffman,0);
        #b) ardenta
        # se alege un cuvant, se scrie codificarea
        # se cloneaza si se fac mici modificari celorlate variante
        # 101100110001010111
        # 01100110001011110
        # 101100110011011010
        # 101100010101111100
        bCuvant = random.choice(dict[Char]);
        # let's get the letter code
        self.codes = {};
        self.getHuffmanCode(self.huffman,"");
        bCode = self.codareHuffman(bCuvant);
        bVariante = [bCode,self.wrongCode(bCode),self.wrongCode(bCode),self.wrongCode(bCode)];
        random.shuffle(bVariante);
        
        
        # se iau cuvinte si se codifica, unele codificari pot fi modificate pt a fi gresite
        cVariante = (self.codareHuffman(random.choice(dict[Char][:-1])),     # rearendat
        self.wrongCode(self.codareHuffman(random.choice(dict[Char][:-1]))),                  # neaderent
        self.wrongCode(self.codareHuffman(random.choice(dict[Char][:-1]))) );                        # arrent
        data = (ponderi,bCuvant,bVariante,cVariante);
        statement = "Primiti urmatoarele litere cu ponderi:\n";
        statement += str(ponderi);
        statement += "\na) Construiti arborele Huffman si afisati codarile literelor\n";
        statement += "b) Care poate fi codarea cuvantului \""+bCuvant+"\"\n";
        for var in bVariante:
            statement += str(var)+"\n";
        statement += "c) Decodati daca se poate:\n";
        for var in cVariante:
            statement += str(var)+"\n";
        statement += "d) Gasiti si alte cuvinte.\n";
        super().__init__(statement,data);
        del self.codes;
        del self.huffman;
        
    def record(self,rec,end="\n"):
        self.solution += str(rec);
        self.solution += str(end);
    
    def minBetween(self,list1,list2):
    # return the minimum from the two list
    # list have element type Node
        if(len(list2) and len(list1)):
            if(list1[0].value[1] > list2[0].value[1]):
                return list2.pop(0);
            else:
                return list1.pop(0);
        elif(len(list1)):
            return list1.pop(0);
        else:
            return list2.pop(0);
        
        
    def makeHuffman(self,list):
        list1 = []; # simple
        list2 = []; # tree nodes
        # se iau litere si se sorteaza intr-o lista
        list1 = list;
        self.record("Se iau caracterele cu ponderile cele mai mici:");
        list1 = sorted(list1, key = lambda x: x[1]);
        # retinem valorile ca fiind niste noduri de arbore
        for i in range(0,len(list1)):
            list1[i] = Node(list1[i]);
        firstTime = True;
        # conventie mai mic la stanga
        while(len(list1) or len(list2) != 1):
            left = self.minBetween(list1,list2);
            right = self.minBetween(list1,list2);
            # new = ("$",left[1]+right[1]);
            new = Node(("$",left.value[1]+right.value[1]),left,right);
            if(firstTime):
                self.record(str(left.value[0])+","+str(left.value[1])+" si "+str(right.value[0])+","+str(right.value[1]));
                self.record("Si facem nodul ce are ca valoare \"$\" si suma ponderilor",":");
                self.record(str(new.value[0])+","+str(new.value[1]));
                self.record("Se aplica acelas procedeu in continuare, alegadu-se cele mai mici ponderi",",");
                self.record("dintre caracterele initiale, dar si noile noduri fomate");
            # new.left = left;
            # new.right = right;
            list2.append(new);
                
        self.huffman = list2[0];
    
    def afisareHuffman(self,root,space):
        if(root.right):
            self.afisareHuffman(root.right,space+4);
        print(" "*space,root.value);
        if(root.left):
            self.afisareHuffman(root.left,space+4);
    
    def wrongCode(self, Hcode):
        hCode = list(Hcode);
        for i in range(0,len(hCode)//2):
            hCode[i] = random.randint(0,1);
        retval = "";
        for c in hCode:
            retval += str(c);
        return retval;    
    
    def dispHuffman(self,root,space):
        if(root.right):
            self.dispHuffman(root.right,space+4);
        self.record(" "*space,"");
        self.record(root.value);
        if(root.left):
            self.dispHuffman(root.left,space+4);
            
            
    def getHuffmanCode(self,root,code):
        # parcurgem arborele in adancime;
        if(root.right):
            self.getHuffmanCode(root.right,code+"1");
        if(root.value[0] != "$"):
            self.codes[root.value[0]] = code;
        if(root.left):
            self.getHuffmanCode(root.left,code+"0");
            
    def codareHuffman(self,cuvant):
    # genereaza codarea Huffman a cucantului
        cod = "";
        for c in cuvant:
            cod+=self.codes[c];
        return cod;
        
    def decodareHuffman(self,theCode):
        Hpos = self.huffman; #position on huffman tree
        word = "";
        for dir in theCode: #dir is direction in the tree
            if(dir == "1"):
                if(Hpos.right):
                    Hpos = Hpos.right;
                else:
                    return None;        #cannot be decoded
            if(dir == "0"):
                if(Hpos.left):
                    Hpos = Hpos.left;
                else:
                    return None;
            if(Hpos.value[0] != "$"):              # is character
                word += Hpos.value[0];
                Hpos = self.huffman;             # rewind the tree pointer
        return word;
        
        
    def findWords(self):
        nrCuv = 3; # vrem doar atatea cuvinte acum
        cuvGasite = 0;
        n = 0;
        cuvinte = [];
        fIn = open("cuvinte.txt","r");
        for word in fIn:    # read line by line
            # word = fIn.readline();
            # facem dictionarul cuvantului
            bifat = True;
            for c in word[1:-1]:
                if c not in self.codes:
                    bifat = False;
                    break;
            if(bifat and word[1:-1]!=''):
                # print(word);
                cuvGasite +=1;
                cuvinte.append(word[1:-1]);
            n+=1;
        if(len(cuvinte)):
            self.record("Cuvinte gasite:");
            for cuv in cuvinte:
                self.record(str(cuv)," ");
        else:
            self.record("Nu s-au gaseit cuvinte");
        # ~ print(cuvinte);
        # ~ print("cuvinte =",cuvGasite);
        # ~ print("cuvinte scanate =",n);
        fIn.close();
        
    def solve(self):
        self.solution = "";
        ponderi = self.data[0];
        # facem arborele
        self.record("a) Se construieste arborele:");
        self.makeHuffman(ponderi);
        self.record("Arborele final:");
        self.dispHuffman(self.huffman,0);
        # let's get the letter code
        self.codes = {};
        self.getHuffmanCode(self.huffman,"");
        self.record("Codarile literelor:");
        for x in self.codes:
            self.record(x,":");
            self.record(self.codes[x]);
        self.record("");
        # punctul b
        # care este codificarea corecta ?
        bCuvant = self.data[1];
        bVariante = self.data[2];
        self.record("b)Care este codarea cuvantului: ","");
        self.record(bCuvant);
        self.record(bVariante);
        self.record("Solutia:"," ");
        self.record(self.codareHuffman(bCuvant));
        self.record("\nc) Decodati daca se poate:")
        cVariante = self.data[3];
        self.record("Se parcurge arborele Huffman dupa \"directiile\" indicate de codare.");
        self.record("Daca urmand sirul nu ajungem la o litera din arbore, atunci sirul nu este o codare valida.");
        for var in cVariante:
            self.record(var,": ");
            sol = self.decodareHuffman(var);
            if(sol):
                self.record(sol);
            else:
                self.record("Nu poate fi decodat");
        # punctul d) gasim si alte cuvinte
        self.record("\nd)");
        self.findWords();
        return self.solution;
        
        

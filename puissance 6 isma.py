matrice=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]] 

joueur_actif=1
def affichage():
    global matrice
    i=7
    for l in range(6):
        g=8
        
        if i==7:
            print("\u001b[1m\u001b[34;1m║0║1║2║3║4║5║6║")
        for c in range (7):
            g-=1
            if g==7:
                if matrice [l][c]==1:
                    print('\u001b[34m║'+('\033[31m'+'☻'+'\033[30m'),end="\u001b[34m║")
                if matrice [l][c]==-1:
                    print('\u001b[34m║'+('\033[33m'+'☻'+'\033[30m'),end="\u001b[34m║")
                if matrice [l][c]==0:
                    print('\u001b[34m║'+' ',end='\u001b[34m║')
            if g>=2 and g<=6:
                if matrice [l][c]==1:
                    print(('\033[31m'+'☻'+'\033[30m'),end="\u001b[34m║")
                if matrice [l][c]==-1:
                    print(('\033[33m'+'☻'+'\033[30m'),end="\u001b[34m║")
                if matrice [l][c]==0:
                    print(' ',end='\u001b[34m║')
            if g==1:
                if matrice [l][c]==1:
                    print(('\033[31m'+'☻'+'\033[30m'),end="\u001b[34m║")
                if matrice [l][c]==-1:
                    print(('\033[33m'+'☻'+'\033[30m'),end="\u001b[34m║")
                if matrice [l][c]==0:
                    print(' ',end='\u001b[34m║')
        
        print("")
        i-=1
        if i == 1: print("\u001b[34m███████████████") 
        

        
        
def victoire():
    # à compléter
    global matrice
    for ligne in range(6):
        for col in range(7):
            
            #test horizontale
            
            if col<=3 and abs(matrice[ligne][col]+matrice[ligne][col+1]+matrice[ligne][col+2]+matrice[ligne][col+3])==4:
                return matrice[ligne][col]
            
            #test verticale
            
            if ligne<=2 and abs(matrice[ligne][col]+matrice[ligne+1][col]+matrice[ligne+2][col]+matrice[ligne+3][col])==4:
                return matrice[ligne][col]
            
            #test diagonale 1
            
            if col<=3 and ligne>=3 and abs(matrice[ligne][col]+matrice[ligne-1][col+1]+matrice[ligne-2][col+2]+matrice[ligne-3][col+3])==4:
                return matrice[ligne][col]
            
            #test diagonale 2
            
            if col<=3 and ligne>=3 and abs(matrice[ligne][col]+matrice[ligne-1][col-1]+matrice[ligne-2][col-2]+matrice[ligne-3][col-3])==4:
                return matrice[ligne][col] 
            
    #tester si le jeu est pas fini 
    
    if abs(matrice[0][0])+abs(matrice[0][1])+abs(matrice[0][2])+abs(matrice[0][3])+abs(matrice[0][4])+abs(matrice[0][5])+abs(matrice[0][6])!=6:
        return 0
    #renvoi que c'est une egalite car il ya personne qui a gagne et tout les cases sont plaines 
    return 2 
def saisie():
    global matrice
    while True:
        l=0     
        coup = input('\u001b[36;1msaisissez votre coup ')
        if coup in ['0','1','2','3','4','5','6']: #tester si le coup appartient aux choix donnes afin de ne pas renvoiyer d'erreurs
            coup=int(coup)

            if matrice[0][coup]!=0:  #tester si la colonne du coup est remplie
                
                print("\u001b[31mcette colonne est remplie, choisissez un autre nombre")
                continue
            else :return coup
        else:print ('\u001b[1m\u001b[31msaisie invalide')
        

def placer_jeton(col,joueur):
    global matrice
    for ligne in range(5,-1,-1): 
        if matrice[ligne][col]==0: #chercher quel ligne est vide dans la colonne choisi commencant de la derniere ligne
            matrice[ligne][col] = joueur
            break
        
        
while victoire()==0: #boucle qui ne s'arrete jusqua qu il ya un gagnant ou que tout les cases sont remple donc une egalite
    affichage() #afficher le jeu
    placer_jeton(saisie(),joueur_actif) #placer le jeton dans la colonne choisi par le joueur
    joueur_actif=-joueur_actif #passage de joueur1 a joueur2
    
if victoire()==1: #si le joueur 1 gagne
    affichage()
    print('\u001b[32mle joueur 1 a gagne !')
if victoire()==-1: #si le joueur 2 gagne
    affichage()
    print("\u001b[32mle joueur 2 a gagne !")
if victoire()==2: #si c'est une egalite
    affichage()
    print("\u001b[32megalite !")


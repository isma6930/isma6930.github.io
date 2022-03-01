matrice=[[0,0,0],[0,0,0],[0,0,0]]
joueur_actif=1
def affichage():
    global matrice
    i=4
    for l in range(3):
        g=4
        for c in range (3):
            g-=1
            if g!=1:
                if matrice [l][c]==1:
                    print('X',end="║")
                if matrice [l][c]==-1:
                    print('O',end="║")
                if matrice [l][c]==0:
                    print(' ',end='║')
            else:
                if matrice [l][c]==1:
                    print('X',end="")
                if matrice [l][c]==-1:
                    print('O',end="")
                if matrice [l][c]==0:
                    print(' ',end='')
        
        print("")
        i-=1
        if i >= 2:
            print("═╬═╬═")

        
        
def victoire():
    global matrice
    if abs(matrice[0][0]+matrice[0][1]+matrice[0][2]) == 3 :
        return  matrice[0][0]
    if abs(matrice[1][0]+matrice[1][1]+matrice[1][2]) == 3 :
        return  matrice[1][0]
    if abs(matrice[2][0]+matrice[2][1]+matrice[2][2]) == 3 :
        return  matrice[2][0]
    if abs(matrice[0][0]+matrice[1][0]+matrice[2][0]) == 3 :
        return  matrice[0][0]
    if abs(matrice[0][1]+matrice[1][1]+matrice[2][1]) == 3 :
        return  matrice[0][1]
    if abs(matrice[0][2]+matrice[1][2]+matrice[2][2]) == 3 :
        return  matrice[0][2]
    if abs(matrice[0][2]+matrice[1][1]+matrice[2][0]) == 3 :
        return  matrice[2][0]
    if abs(matrice[0][0]+matrice[1][1]+matrice[2][2]) == 3 :
        return  matrice[0][0]
    if abs(matrice[2][0]+matrice[0][1]+matrice[0][2]) == 3 :
        return  matrice[2][0]
    for i in range(3):
        for j in range(3):
            if matrice[i][j]==0:
                return 0
    return 2
def saisie():

    global matrice
    while True:
        print('0','/','1','/','2')
        print('3','/','4','/','5')
        print('6','/','7','/','8')
        if joueur_actif== 1:
            coups= int(input('choisir une case joueur 1 '))
        if joueur_actif== -1:
            coups= int(input('choisir une case joueur 2 '))
        if matrice[coups//3][coups%3]!=0:
            print("choisir un autre nombre")
            continue
        return coups
def IA_joue():
    global matrice
    liste_defaut=[4,8,0,2,6,1,5,3,7]
    for coup in range(9):
        if matrice[coup//3][coup%3]== 0:
            matrice[coup//3][coup%3] = -1
            if victoire()== -1 :
                return coup
            else :
                matrice[coup//3][coup%3] = 0
            
    for coup in range(9):
        if matrice[coup//3][coup%3]== 0:
            matrice[coup//3][coup%3] = 1
            if victoire()== 1 :
                return coup
            else :
                matrice[coup//3][coup%3] = 0
    for coup in liste_defaut:
        if matrice[coup//3][coup%3]== 0:
            return coup
        
    
            
while victoire()==0:
    affichage()
    if joueur_actif==1: coup=saisie()
    else : coup=IA_joue()
   
    matrice[coup//3][coup%3] = joueur_actif
    joueur_actif=-joueur_actif
    print("")
if victoire()==1:
    affichage()
    print('le joueur 1 a gagne !')
if victoire()==-1:
    affichage()
    print("l'IA a gagne !")
if victoire()==2:
    affichage()
    print("egalite !")
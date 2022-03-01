'''

 ___   _______  __   __  _______  _______  _______  ___      ___      _______   
|   | |       ||  |_|  ||   _   ||  _    ||   _   ||   |    |   |    |       |  
|   | |  _____||       ||  |_|  || |_|   ||  |_|  ||   |    |   |    |  _____|  
|   | | |_____ |       ||       ||       ||       ||   |    |   |    | |_____   
|   | |_____  ||       ||       ||  _   | |       ||   |___ |   |___ |_____  |  
|   |  _____| || ||_|| ||   _   || |_|   ||   _   ||       ||       | _____| |  
|___| |_______||_|   |_||__| |__||_______||__| |__||_______||_______||_______|  
'''
matrice= [[8,0,0,0,0,0,0,0,0],
          [0,0,3,6,0,0,0,0,0],
          [0,7,0,0,9,0,2,0,0],
          [0,5,0,0,0,7,0,0,0],
          [0,0,0,0,4,5,7,0,0],
          [0,0,0,1,0,0,0,3,0],
          [0,0,1,0,0,0,0,6,8],
          [0,0,8,5,0,0,0,1,0],
          [0,9,0,0,0,0,4,0,0]]

def test(i,j):
    global matrice
    # test de la ligne
    # test de la colonne
    # test du cadrant
    for col in range(9):
        if col != j:
            if matrice[i][col]==matrice[i][j] : return False
    for ligne in range(9):
        if ligne != i:
            if matrice[ligne][j]==matrice[i][j] : return False

        
    for ligne in range ((i//3)*3,(i//3)*3+3):
        for col in range((j//3)*3,(j//3)*3+3):
            if ligne != i and col != j:
                if matrice[ligne][col]==matrice[i][j] : return False
    return True  # si aucun des test précédent n'a renvoyé False c'est que la grille est bonne

def solver(i=0,j=0):
    global matrice
    if i==9:
        
        for ligne in range (9):
            print (matrice[ligne])  #l'affichage pourrait être amélioré
    
    else:

        if matrice[i][j]!=0 : # on est sur une case déja remplie qu'il ne faut pas modifier
            if j+1<=8:solver(i,j+1)
            else:
                solver(i+1,0)
            # passe récursivement à la case suivante
        else :
            for chiffre in range(1,10): # je test les 9 possibilités
                matrice[i][j]=chiffre
                if test(i,j)== True :
                    if j+1<=8:
                        solver(i,j+1)
                    else :
                        solver(i+1,0)
                matrice[i][j]=0
                # si la matrice est bonne, je passe récursivement à la case d'apprès
            # je n'oublie pas de remettre la case [i][j] à 0 avant de finir les cas possibles pour ce traitement du cas i,j	
solver()
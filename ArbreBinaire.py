class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur  
        self.gauche = None     
        self.droite = None     

def creer_arbre(formule):
    if len(formule) == 0:
        return None 

    niveau = 0           
    index = -1           

   
    for i in range(len(formule) - 1, -1, -1):
        if formule[i] == ')':
            niveau += 1   
        elif formule[i] == '(':
            niveau -= 1   
        elif niveau == 0 and (formule[i] == '&' or formule[i] == '|' or (formule[i] == '~' and i == 0)):
            index = i     
            break

    
    if index != -1 and formule[index] == '~' and index > 0:
        index = -1

    if index != -1:
        
        noeud = Noeud(formule[index])
        noeud.gauche = creer_arbre(formule[:index])
        noeud.droite = creer_arbre(formule[index + 1:])
        return noeud

    if formule[0] == '(' and formule[-1] == ')':
        return creer_arbre(formule[1:-1])

    return Noeud(formule)

def afficher_arbre(noeud, niveau=0):
    if noeud:
        print('    ' * niveau + str(noeud.valeur)) 
        afficher_arbre(noeud.gauche, niveau + 1)    
        afficher_arbre(noeud.droite, niveau + 1)    

formule_utilisateur = input("Entrez la formule logique : ")
arbre_utilisateur = creer_arbre(formule_utilisateur)
afficher_arbre(arbre_utilisateur)


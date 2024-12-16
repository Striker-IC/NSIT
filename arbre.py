def taille(arbre:dict, lettre:str) -> int:
    if lettre == '':
        return 0
    else:
        return taille(arbre, arbre[lettre][0]) and taille(arbre, arbre[lettre][1])
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
assert taille(a, 'F') == 9
assert taille(a, 'B') == 5
assert taille(a, 'I') == 2
#%% Nagsarkar Ex 9.3

X = [44.8,110.4,80.6]
If = -3.222j
U0 = 1
Zaux = 0.001j
Uf = [(U0-If*Zaux*x) for x in X]

# Node voltages
for uf in Uf:
    print("{:.3e}".format(uf))
    
li_branch_aux = [
    [1,2,200],
    [2,3,250],
    [3,1,300]]
for n in li_branch_aux:
    [a, b] = [n[0]-1, n[1]-1] 
    [Ufa, Ufb] = [Uf[a], Uf[b]]
    zab = n[2]*Zaux
    Ifab = (Ufa-Ufb)/zab
    print(f"If({a+1},{b+1}): {Ifab}")
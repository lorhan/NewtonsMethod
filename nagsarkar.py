#%% Nagsarkar Ex 9.3

X = [44.8,110.4,80.6]
If = -3.222j
U0 = 1
Zaux = 0.001j
Uf = [(U0-If*Zaux*x) for x in X]

# Node voltages
for uf in Uf:
    print("{:.3e}".format(uf))


# Branch currents
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


#%% Nagsarkar 10 exploring symm comp
# https://www.sympy.org/de/shell.html

from sympy import *
init_printing()

za = symbols("z_{a}")
zab = symbols("z_{ab}")
zac = symbols("z_{ac}")
zb = symbols("z_{b}")
zbc = symbols("z_{bc}")
zc = symbols("z_{c}")
Zabc = symbols("Z_{abc}")
Zabc = Matrix([[za,zab,zac],[zab,zb,zbc],[zac,zbc,zc]])


a = symbols(r"\alpha")

A = Matrix([[1,1,1],[1,a**2,a],[1,a,a**2]])
Ainv = (A**-1).subs([(a**3,1),(a**4,a),(a**2+a,-1),(a+1,-a**2),(a**2+1,-a),(1/a,a**2)])


Z012 = symbols("Z_{012}")
Z012_v1 = Ainv*Zabc*A
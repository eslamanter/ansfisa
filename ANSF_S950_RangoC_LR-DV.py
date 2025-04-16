def aqI(I):
    k = 104
    return I / k


def I(V, R, D):
    k = 8.025
    return k * (V ** 2) / R - D


def Psi(aq, V, L):
    return (aq * V) / (3.6 * L)


def dIdt(Psi):
    k = 104
    return k * Psi


def dDdt(D, V, L):
    return (D * V) / (3.6 * L)


def Omega(D, I, V):
    k = 3672
    return (D / I) * V / k


def dDdL(D, L):
    return D / L


def LimANSF(L, R, D, V):
    Tutto_ok = True
    if aqI(I(V, R, D)) > 1:
        Tutto_ok = False
    if I(V, R, D) > 104:
        Tutto_ok = False
    if Psi(aqI(I(V, R, D)), V, L) > 0.7:
        Tutto_ok = False
    if dIdt(Psi(aqI(I(V, R, D)), V, L)) > 73:
        Tutto_ok = False
    if dDdt(D, V, L) > 80:
        Tutto_ok = False
    if Omega(D, I(V, R, D), V) > 0.078:
        Tutto_ok = False
    if dDdL(D, L) > 3:
        Tutto_ok = False
    return Tutto_ok


for Vmax in range(30, 141, 5):
    try:
        with open(f'{Vmax}.txt') as file:
            testo = file.readlines()
        stampa = ''
        for riga in testo:
            riga = riga.split('\t')
            try:
                L = float(riga[0].replace('\n', ''))
                R = float(riga[1].replace('\n', ''))
                V, V_ok = Vmax, False
                while not V_ok:
                    for D in range(110, -1, -5):
                        if LimANSF(L, R, D, V):
                            V_ok = True
                            Dmin = D
                    if not V_ok:
                        V -= 5
                stampa += f'{riga[0].replace('\n', '')}\t{riga[1].replace('\n', '')}\t{Dmin}\t{V}\n'
            except:
                try:
                    stampa += f'{riga[0].replace('\n', '')}\t'
                except:
                    stampa += '\t'
                try:
                    stampa += f'{riga[1].replace('\n', '')}\n'
                except:
                    stampa += '\n'
        with open(f'{Vmax}.txt', 'w') as file:
            file.write(stampa)
        break
    except:
        pass
raise SystemExit

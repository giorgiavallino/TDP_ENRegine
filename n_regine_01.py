from time import time

class NRegine:

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0

    def solve(self, n):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self._ricorsione([], n)

    def isAdmissible(self, regina_01, regina_02):
        # Verificare la riga: se non va bene, return False -->
        if regina_01[0] == regina_02[0]:
            return False
        # Verificare la colonna: se non va bene, return False -->
        if regina_01[1] == regina_02[1]:
            return False
        # Verificare la prima diagonale: se non va bene, return False -->
        if regina_01[0] + regina_01[1] == regina_02[0] + regina_02[1]:
            return False
        # Verificare la seconda diagonale: se non va bene, return False -->
        if regina_01[0] - regina_01[1] == regina_02[0] - regina_02[1]:
            return False
        # Se tutti i controlli sono andati a buon fine, return True -->
        return True

    def isSoluzione(self, soluzione_parziale):
        for i in range(len(soluzione_parziale)-1):
            for j in range(i+1, len(soluzione_parziale)):
                result = self.isAdmissible(soluzione_parziale[i], soluzione_parziale[j])
                # Se almeno un risultato è falso, la soluzione parziale non è ammissibile:
                if result == False:
                    return False
        return True

    def _ricorsione(self, soluzione_parziale, n): # --> è il metodo che verrà chiamato più volte
        self.n_chiamate = self.n_chiamate + 1 # serve per un'analisi statistica: quante chiamate al metodo ricorsivo
        # sono state fatte?
        # Condizione terminale: quando la soluzione_parziale ha lunghezza n, ossia quando si hanno n regine = si è
        # raggiunta una possibile soluzione
        if len(soluzione_parziale) == n:
            # Bisogna verificare se la soluzione_parziale possibile trovata è ammissibile come soluzione del problema:
            if self.isSoluzione(soluzione_parziale):
                print(soluzione_parziale)
                self.n_soluzioni = self.n_soluzioni + 1 # serve per un'analisi statistica: quante soluzioni possibili
                # sono state trovate?
        # Caso ricorsivo
        else:
            for riga in range(n):
                for colonna in range(n):
                    soluzione_parziale.append([riga, colonna]) # --> viene provata una nuova ipotesi = si aggiunge un
                    # pezzo della possibile soluzione
                    self._ricorsione(soluzione_parziale, n) # --> si prosegue con la ricorsione
                    soluzione_parziale.pop() # --> backtracking


if __name__ == '__main__':
    nreg = NRegine()
    start_time = time()
    nreg.solve(4)
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}.")
    print(f"Ho trovato {nreg.n_soluzioni} (possibili) soluzioni.")
    print(f"Numero chiamate ricorsive: {nreg.n_chiamate}.")
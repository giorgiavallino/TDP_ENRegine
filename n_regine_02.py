# Viene introdotto un altro metodo che verifica che le soluzioni possibili siano ammissibili: in questo caso, però,
# il metodo di verifica viene chiamato ogni qual volta viene introdotta una nuova regina --> in questo modo, se una
# nuova regina viene aggiunta in un posto non ammesso, la soluzione possibile viene immediatamente scartata senza
# inserire le restanti regine
# Questo metodo è più efficiente: viene usato il metodo ricorsivo meno volte!

import copy
from time import time

class NRegine:

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = [] # --> viene introdotta una nuova variabile: essa serve per verificare che una soluzione non
        # sia già presente (magari semplicemente con un ordine diverso)

    def solve(self, n):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
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

    def isValid(self, nuova_regina, soluzione_parziale):
        for regina in soluzione_parziale:
            if not self.isAdmissible(nuova_regina, regina):
                return False
        return True

    def _ricorsione(self, soluzione_parziale, n): # --> è il metodo che verrà chiamato più volte
        self.n_chiamate = self.n_chiamate + 1 # serve per un'analisi statistica: quante chiamate al metodo ricorsivo
        # sono state fatte?
        # Condizione terminale: quando la soluzione_parziale ha lunghezza n, ossia quando si hanno n regine = si è
        # raggiunta una possibile soluzione
        if len(soluzione_parziale) == n:
            # Verificare se la soluzione sia già stata trovata:
            self.soluzioni.append(copy.deepcopy(soluzione_parziale)) # si sarebbero potuti usare anche dei dizionari e
            # degli insiemi, al posto delle liste --> da qui bisognerebbe andare avanti con nuove righe di codice ed
            # eventuali metodi per verificare che la soluzione non sia già presente...
            print(soluzione_parziale)
            self.n_soluzioni = self.n_soluzioni + 1 # serve per un'analisi statistica: quante soluzioni possibili
            # sono state trovate?
        # Caso ricorsivo
        else:
            for riga in range(n):
                for colonna in range(n):
                    # Verificare che la nuova regina che viene aggiunta sia aggiunta in una posizione ammissibile:
                    nuova_regina = [riga, colonna]
                    if self.isValid(nuova_regina, soluzione_parziale):
                        soluzione_parziale.append([riga, colonna]) # --> viene provata una nuova ipotesi = si aggiunge
                        # un pezzo della possibile soluzione
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
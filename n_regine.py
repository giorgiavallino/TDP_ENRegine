import copy
from time import time


class NRegine():

    def __init__(self):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []


    def solve(self, N):
        self.n_soluzioni = 0
        self.n_chiamate = 0
        self.soluzioni = []
        self._ricorsione([], N)

    def is_admissible(self, regina1, regina2) -> bool:
        #1) verifico riga. Se non va bene, return False
        if regina1[0] == regina2[0]:
            return False
        #2) verifico colonna. Se non va bene, return False
        if regina1[1] == regina2[1]:
            return False
        #3) verifico diagonale 1. Se non va bene, return False
        if regina1[0]+regina1[1] == regina2[0]+regina2[1]:
            return False
        #4) verifico diagonale 2. Se non va bene, return False
        if regina1[0]-regina1[1] == regina2[0]-regina2[1]:
            return False
        #5) Ho passato tutti i controlli. Return true
        return True

    def is_soluzione(self, parziale):
        for i in range(len(parziale)-1):
            for j in range(i+1, len(parziale)):
                result = self.is_admissible(parziale[i], parziale[j])
                if result == False:
                    return False
        return True

    def is_valid(self, nuova_regina, parziale):
        for regina in parziale:
            if not self.is_admissible(nuova_regina, regina):
                return False
        return True


    def _ricorsione(self, parziale, N):
        self.n_chiamate += 1

        #condizione terminale: quando parziale ha lunghezza N
        if len(parziale)==N:
            # => verifico se questa è una soluzione
            # if self.is_soluzione(parziale):

            #verifica se è una soluzione già trovata
            print(parziale)
            self.soluzioni.append(copy.deepcopy(parziale))
            self.n_soluzioni += 1
        # caso ricorsivo
        else:
            for riga in range(N):
                for col in range(N):
                    # => Check sulla regina che vado ad aggiungere
                    nuova_regina = [riga, col]
                    if self.is_valid(nuova_regina, parziale):
                        #provo nuova ipotesi
                        parziale.append([riga, col])
                        #vado avanti nella ricorsione
                        self._ricorsione(parziale, N)
                        # backtracking
                        parziale.pop()



if __name__ == '__main__':
    nreg = NRegine()
    start_time = time()
    nreg.solve(4)
    end_time = time()
    print(f"Elapsed time: {end_time - start_time}")
    print(f"Ho trovato {nreg.n_soluzioni} (possibili) soluzioni")
    print(f"N. chiamate ricorsive: {nreg.n_chiamate}")
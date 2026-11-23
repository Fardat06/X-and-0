class Tabla:
    def __init__(self):
        self.celula = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]

    def afisare(self):
        print(" %s | %s | %s |" % (self.celula[1], self.celula[2], self.celula[3]))
        print(" %s | %s | %s |" % (self.celula[4], self.celula[5], self.celula[6]))
        print(" %s | %s | %s |" % (self.celula[7], self.celula[8], self.celula[9]))

    def urmatorulpas(self, jucator, numarcelula):
        if numarcelula < 1 or numarcelula > 9:
            print("Nu ai pus un numar valid, pune te rog unul intre 1 si 9!")
            return False

        if self.celula[numarcelula] == ".":
            self.celula[numarcelula] = jucator
            return True
        else:
            print("Este deja pus un simbol acolo, pune in alt loc!")
            return False

    def castigator(self, jucator):
        combinatii = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]

        for a, b, c in combinatii:
            if self.celula[a] == self.celula[b] == self.celula[c] == jucator:
                return True

        return False

    def egalitate(self):
        for i in range(1, 10):
            if self.celula[i] == ".":
                return False

        return True

    def mesajdeinceput(self):
        print("Bun venit la un joc de X si 0")


def minimax(tabla, adancime, este_maximizare):
    if tabla.castigator("X"):
        return 10 - adancime

    if tabla.castigator("0"):
        return adancime - 10

    if tabla.egalitate():
        return 0

    if este_maximizare:
        cel_mai_bun_scor = -1000

        for i in range(1, 10):
            if tabla.celula[i] == ".":
                tabla.celula[i] = "X"

                scor = minimax(tabla, adancime + 1, False)

                tabla.celula[i] = "."

                cel_mai_bun_scor = max(cel_mai_bun_scor, scor)

        return cel_mai_bun_scor

    else:
        cel_mai_bun_scor = 1000

        for i in range(1, 10):
            if tabla.celula[i] == ".":
                tabla.celula[i] = "0"

                scor = minimax(tabla, adancime + 1, True)

                tabla.celula[i] = "."

                cel_mai_bun_scor = min(cel_mai_bun_scor, scor)

        return cel_mai_bun_scor


def mutare_computer(tabla):
    cel_mai_bun_scor = 1000
    cea_mai_buna_mutare = None

    for i in range(1, 10):
        if tabla.celula[i] == ".":
            tabla.celula[i] = "0"

            scor = minimax(tabla, 0, True)

            tabla.celula[i] = "."

            if scor < cel_mai_bun_scor:
                cel_mai_bun_scor = scor
                cea_mai_buna_mutare = i

    tabla.urmatorulpas("0", cea_mai_buna_mutare)

    print("\nComputerul a ales celula:", cea_mai_buna_mutare)


tabla = Tabla()

tabla.mesajdeinceput()

print("\nTu esti X.")
print("Computerul este 0.")

tabla.afisare()


while True:

    while True:
        try:
            alegeraluix = int(input("\nX) Alege un nr de la 1 la 9: "))

            if tabla.urmatorulpas("X", alegeraluix):
                break

        except ValueError:
            print("Te rog introdu un numar!")

    tabla.afisare()

    if tabla.castigator("X"):
        print("X este castigatorul!")
        break

    if tabla.egalitate():
        print("Este egalitate!")
        break


    print("\nComputerul gandeste...")

    mutare_computer(tabla)

    tabla.afisare()

    if tabla.castigator("0"):
        print("0 este castigatorul!")
        print("Computerul a castigat!")
        break

    if tabla.egalitate():
        print("Este egalitate!")
        break

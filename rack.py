from node import Node

class Rack:
    def __init__(self):
        self._listeMedNoder = []


        # Rack inneholder en liste med maks antall noder i.


    def settInn(self, node):
        self._listeMedNoder.append(node)

    # Oppretter en metode som legger til en node i listen med noder.


    def getAntNoder(self):
        return len(self._listeMedNoder)

    # For å ha kontroll på lengden av listen, dvs antall noder i listen, opretter vi en metode som vi kan eventuelt kalle på
    # når vi trenger å vite om det er plass til flere noder i listen.

    def antProsessorer(self):
        AntallPros = 0
        for node in self._listeMedNoder:
            AntallPros += node.antProsessorer()
            return AntallPros

    # Lager en variabel AntallPros inni en metode for å trekke ut hvor mange prosesssorer det er i listen.

    def noderMedNokMinne(self, paakrevdMinne):

        AntallNod = 0
        for node in self._listeMedNoder:
            if node.nokMinne(paakrevdMinne) is True:
                AntallNod += 1
        return AntallNod

    # Her gjør det det samme. Vi bruker funksjon nokMinne fra node.py til å kunne telle opp om hver node i listen
    # har påkrevd minne.

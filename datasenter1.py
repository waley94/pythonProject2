from node import Node
from regneklynge import Regneklynge

class Datasenter:
    def __init__(self): # opretter en ordbok av regneklynger
        self._ordbok = {}

    def lesInnRegneklynge(self, filnavn): #lager en funksjon som leser
        fil = open(filnavn, "r")
        navn = filnavn
        liste1 = []
        for linje in fil:
            liste1.append(linje)
        MaxNoderPerRack  = int(liste1[0])
        r = Regneklynge(MaxNoderPerRack)
        liste2 = []
        liste2 = liste1.copy()
        liste2.pop(0)
        for linje in liste2:
            Del = linje.split(' ')
            AntallNoder = int(Del[0])
            MinnePerNode = int(Del[1])
            AntallProsessorerPerNode = int(Del[2])
            node = Node(MinnePerNode, AntallProsessorerPerNode)
            r.settInnNode(node)

            self._ordbok[navn] = r

    def skrivUtAlleRegneklynger(self):
        for keys in self._ordbok:
            print()
            self.skrivUtAlleRegneklynger(keys)


    def SkrivUtRegneklynge(self, navn):
        k = self._ordbok[navn]

        racks = k.antRacks()
        antPros = k.antProsessorer()
        n32 = k.noderMedNokMinne(32)
        n64 = k.noderMedNokMinne(64)
        n128 = k.noderMedNokMinne(128)

        print('informasjon om regneklyngen', navn)

        print('Antall rack:', racks)
        print('Antall prosessorer:',antPros)
        print('Noder med minst 32 GB:', n32)
        print('Noder med minst 64 GB:', n64)
        print('Noder med minst 128 GB:', n128)
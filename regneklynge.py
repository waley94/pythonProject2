from rack import Rack

class Regneklynge:

    def __init__(self, noderPerRack):
        self._listeMedRacks = []
        self._noderPerRack = noderPerRack

        # oppretter en regneklynge og setter maks antall noder per rack. Dette er fordi
        # regneklyngen m책 basere seg p책 hvor mange noder racks i regneklyngen kan ta for seg.

    def settInnNode(self, node):
            if len(self._listeMedRacks) == 0:
                self._listeMedRacks.append(Rack())
            for e in self._listeMedRacks:
                if e.getAntNoder() < self._noderPerRack:
                    e.settInn(node)
                elif self._listeMedRacks[-1].getAntNoder( ) == self._noderPerRack:
                    self._listeMedRacks.append(Rack())

    # Her lager jeg en metode som tar for seg en node i listen om det er plass i listen. S책 det vil si om lengden
    # av antall noder i listen er lik regneklynge(noderPerRack), s책 vil det lages en ny Rack liste med maks noder i.


    def antProsessorer(self):
        antPros = 0
        for rack in self._listeMedRacks:
            antPros += rack.antProsessorer()
        return antPros

    # beregner antall prosessorer i regneklyngen og returnerer verdien.

    def noderMedNokMinne(self, paakrevdMinne):
        antallNod = 0
        for racks in self._listeMedRacks:
            antallNod += racks.noderMedNokMinne(paakrevdMinne)
        return  antallNod

    # beregner antall rack i listen

    def antRacks(self):
        return len(self._listeMedRacks)
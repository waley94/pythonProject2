class Node:

    def __init__(self, minne, antPros):
        self._minne = minne
        self._antPros = antPros
        # Oppretter Node som inneholder ønsket minnestørrelse og antall prosessorer


    def antProsessorer(self):
        if self._antPros == 2 or self._antPros ==1 :
            return self._antPros
        else:
            return None
    # returnerer verdien som handler om hvor mange prosessorer noden har. Per node kan maks ha to eller mindre antPros.

    def nokMinne(self, paakrevdMinne):
        self._paakrevdMinne = paakrevdMinne
        if self._minne >= self._paakrevdMinne:
            return True
        else:
            return False
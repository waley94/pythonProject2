from node import Node
from regneklynge import Regneklynge


def hovedprogram():
    # Oppretter RegneKlynge og noder.
    abel = Regneklynge(12)
    for e in range(650):
        abel.settInnNode(Node(64, 1))
    for i in range(16):
        abel.settInnNode(Node(1024, 2))
    # Printer ut kriteriene.
    print("Noder med minst 32 GB:", abel.noderMedNokMinne(32))
    print("Noder med minst 64 GB:", abel.noderMedNokMinne(64))
    print("Noder med minst 128 GB:", abel.noderMedNokMinne(128))
    print("Antall prosessorer:", abel.antProsessorer())
    print("Antall rack:", abel.antRacks())

    # Oppretter RegneKlynge og noder.
    saga = Regneklynge(8)
    for e in range(264):
        saga.settInnNode(Node(64, 1))
    for i in range(8):
        saga.settInnNode(Node(1024, 2))
    # Printer ut kriteriene.
    print("Noder med minst 32 GB:", saga.noderMedNokMinne(32))
    print("Noder med minst 64 GB:", saga.noderMedNokMinne(64))
    print("Noder med minst 128 GB:", saga.noderMedNokMinne(128))
    print("Antall prosessorer:", saga.antProsessorer())
    print("Antall rack:", saga.antRacks())


hovedprogram(

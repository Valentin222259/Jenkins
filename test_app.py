from app import adunare, scadere


def test_adunare():
    assert adunare(2, 3) == 5


def test_scadere():
    assert scadere(5, 2) == 3  # Comentariu corect cu doua spatii inainte

from app import adunare, scadere


def test_adunare():
    assert adunare(2, 3) == 5


def test_scadere():
    # Comentariul este acum deasupra pentru a evita linia prea lunga
    assert scadere(5, 2) == 3

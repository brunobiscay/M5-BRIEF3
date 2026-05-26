from modules.calcul import calcul_carre


def test_calcul_carre():
    assert calcul_carre(2) == 4
    assert calcul_carre(-3) == 9
    assert calcul_carre(0) == 0

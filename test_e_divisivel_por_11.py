from e_divisivel_por_11 import e_divisivel_por_11

def test_e_divisivel_por_11_dois_digitos_positivo():
    assert e_divisivel_por_11(11) == True
    assert e_divisivel_por_11(22) == True
    assert e_divisivel_por_11(33) == True
    assert e_divisivel_por_11(44) == True
    assert e_divisivel_por_11(55) == True
    assert e_divisivel_por_11(66) == True
    assert e_divisivel_por_11(77) == True
    assert e_divisivel_por_11(88) == True
    assert e_divisivel_por_11(99) == True

def test_nao_e_divisivel_por_11_dois_digitos_positivo():
    assert e_divisivel_por_11(12) == False
    assert e_divisivel_por_11(23) == False
    assert e_divisivel_por_11(32) == False
    assert e_divisivel_por_11(45) == False

def test_e_divisivel_por_11_dois_digitos_negativo():
    assert e_divisivel_por_11(-11) == True
    assert e_divisivel_por_11(-22) == True
    assert e_divisivel_por_11(-33) == True
    assert e_divisivel_por_11(-44) == True
    assert e_divisivel_por_11(-55) == True
    assert e_divisivel_por_11(-66) == True
    assert e_divisivel_por_11(-77) == True
    assert e_divisivel_por_11(-88) == True
    assert e_divisivel_por_11(-99) == True

def test_nao_e_divisivel_por_11_dois_digitos_negativo():
    assert e_divisivel_por_11(-12) == False
    assert e_divisivel_por_11(-23) == False
    assert e_divisivel_por_11(-32) == False
    assert e_divisivel_por_11(-45) == False

def test_e_divisivel_por_11_entre_100_e_200_positivo():
    assert e_divisivel_por_11(110) == True
    assert e_divisivel_por_11(121) == True
    assert e_divisivel_por_11(132) == True
    assert e_divisivel_por_11(143) == True
    assert e_divisivel_por_11(154) == True
    assert e_divisivel_por_11(165) == True
    assert e_divisivel_por_11(176) == True
    assert e_divisivel_por_11(187) == True
    assert e_divisivel_por_11(198) == True

def test_e_divisivel_por_11_entre_100_e_200_negativo():
    assert e_divisivel_por_11(-110) == True
    assert e_divisivel_por_11(-121) == True
    assert e_divisivel_por_11(-132) == True
    assert e_divisivel_por_11(-143) == True
    assert e_divisivel_por_11(-154) == True
    assert e_divisivel_por_11(-165) == True
    assert e_divisivel_por_11(-176) == True
    assert e_divisivel_por_11(-187) == True
    assert e_divisivel_por_11(-198) == True

def test_e_divisivel_por_11_maior_que_200_positivo():
    assert e_divisivel_por_11(209) == True
    assert e_divisivel_por_11(297) == True
    assert e_divisivel_por_11(330) == True
    assert e_divisivel_por_11(352) == True
    assert e_divisivel_por_11(374) == True
    assert e_divisivel_por_11(440) == True
    assert e_divisivel_por_11(990) == True
    assert e_divisivel_por_11(4103) == True
    assert e_divisivel_por_11(4180) == True
    assert e_divisivel_por_11(4301) == True
    assert e_divisivel_por_11(5390) == True
    assert e_divisivel_por_11(6380) == True
    assert e_divisivel_por_11(6402) == True
    assert e_divisivel_por_11(6413) == True

def test_e_divisivel_por_11_maior_que_200_negativo():
    assert e_divisivel_por_11(-209) == True
    assert e_divisivel_por_11(-297) == True
    assert e_divisivel_por_11(-330) == True
    assert e_divisivel_por_11(-352) == True
    assert e_divisivel_por_11(-374) == True
    assert e_divisivel_por_11(-440) == True
    assert e_divisivel_por_11(-990) == True
    assert e_divisivel_por_11(-4103) == True
    assert e_divisivel_por_11(-4180) == True
    assert e_divisivel_por_11(-4301) == True
    assert e_divisivel_por_11(-5390) == True
    assert e_divisivel_por_11(-6380) == True
    assert e_divisivel_por_11(-6402) == True
    assert e_divisivel_por_11(-6413) == True

def test_nao_e_divisivel_por_11_maior_que_200_positivo():
    assert e_divisivel_por_11(210) == False
    assert e_divisivel_por_11(212) == False
    assert e_divisivel_por_11(6381) == False
    assert e_divisivel_por_11(6382) == False
    assert e_divisivel_por_11(10000) == False
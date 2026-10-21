from project import check_status, check_age, check_heart_rate

def test_check_status():
    # Casos válidos
    assert check_status("Alive") == True
    assert check_status("Dead") == True

    # Casos inválidos
    assert check_status("Unknown") == False
    assert check_status("alive") == False  # Case-sensitive check
    assert check_status("Zombi") == False

def test_check_age():
    # Casos válidos (límites y normales)
    assert check_age("0") == True
    assert check_age("45") == True
    assert check_age("120") == True

    # Casos inválidos (fuera de rango y letras)
    assert check_age("-1") == False
    assert check_age("121") == False
    assert check_age("NA") == False
    assert check_age("cuarenta") == False

def test_check_heart_rate():
    # Casos válidos (límites y normales)
    assert check_heart_rate("30") == True
    assert check_heart_rate("75") == True
    assert check_heart_rate("250") == True

    # Casos inválidos (fuera de rango y letras)
    assert check_heart_rate("29") == False
    assert check_heart_rate("251") == False
    assert check_heart_rate("unknown") == False
    assert check_heart_rate("-50") == False

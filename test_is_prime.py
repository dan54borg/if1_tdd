from main import is_prime

def test_is_prime_happy():
    assert is_prime (2) == True
    assert is_prime (3) == True
    assert is_prime (7) == True

def test_is_prime_unhappy():
    assert is_prime (1) == False
    assert is_prime (4) == False


from square_calculator import square


def test_square_of_positive():
    assert square(2) == 4
    assert square(10) == 100

def test_square_of_negative():
    assert square(-3) == 9
    assert square(-1) == 1
    
    
def test_square_of_zero():
    assert square(0) == 0
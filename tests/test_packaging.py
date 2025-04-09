def test_import():
    from dartproject.utils import cart2pol
    phi, r = cart2pol(1,1)

    assert abs(phi-3.1415/4) < 0.01
    assert abs(r-2**0.5) < 0.01

def test_import2():
    from dartproject.utils import pol2cart
    x, y = pol2cart(90*3.1415/180,1)
    assert abs(x-0) < 0.01
    assert abs(y-1) < 0.01

def test_utils():
    try:
        import dartproject.utils
        x = True
    except ModuleNotFoundError:
        x = False
    assert x

def test_findBest():
    try:
        import dartproject.findBest
        x = True
    except ModuleNotFoundError:
        x = False
    assert x

def test_scoring():
    try:
        import dartproject.scoring
        x = True
    except ModuleNotFoundError:
        x = False
    assert x

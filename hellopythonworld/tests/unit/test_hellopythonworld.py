from hellopythonworld.hellopythonworld import HelloPythonWorld

def test_square():
    new_hellopythonworld = HelloPythonWorld()
    assert new_hellopythonworld.square(3) == 9

def test_cube():
    new_hellopythonworld = HelloPythonWorld()
    assert new_hellopythonworld.cube(3) == 27

def test_quad():
    new_hellopythonworld = HelloPythonWorld()
    assert new_hellopythonworld.quad(3) == 81


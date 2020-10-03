import ballometer


def test_temperature():
    b = ballometer.BMP()
    assert 250.0 < b.temperature < 350.0


def test_pressure():
    b = ballometer.BMP()
    assert 300.0 * 1e2 < b.pressure < 1100.0 * 1e2
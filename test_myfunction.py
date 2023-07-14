import pytest

from myfunction import calculate_sphere_area, calculate_sphere_volume

def test_calculate_sphere_area():
    radius = 10 
    area = calculate_sphere_area(radius)
    # should be around 1256.64
    assert pytest.approx(area, 0.01) == 1256.64

def test_calculate_sphere_volume():
    radius = 3.2 
    area = calculate_sphere_volume(radius)
    # should be around 137.26
    assert pytest.approx(area, 0.01) == 137.26

def test_calculate_sphere_volume2():
    radius = 100
    area = calculate_sphere_volume(radius)
    # should be around 137.26
    assert pytest.approx(area, 0.01) == 137.26


    
# To test, run:
# $ pytest
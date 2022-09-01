# test_capitalize.py
import pytest
# TUTORIAL

def capital_case(x):
    return x.capitalize()

@pytest.mark.skip
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
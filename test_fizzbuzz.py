from main import fizzbuzz

def test_pytest():
    assert 1 + 2 == 3
    assert 2 + 3 == 5

def test_fizzbuzz_nothing():
    assert fizzbuzz(2) == 2
    assert fizzbuzz(7) == 7

def test_fizzbuzz_fizz():
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(9) == "fizz"

def test_fizzbuzz_buzz():
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(20) == "buzz"

def test_fizzbuzz_fizzbuzz():
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(45) == "fizzbuzz"
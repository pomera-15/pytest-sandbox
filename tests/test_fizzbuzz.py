import pytest
from src.fizzbuzz import FizzBuzz


@pytest.fixture
def fizzbuzz():
    fizzbuzz = FizzBuzz()
    return fizzbuzz


def test_3の倍数でFizzを返す(fizzbuzz):
    assert fizzbuzz.convert(3) == "Fizz"


def test_5の倍数でBuzzを返す(fizzbuzz):
    assert fizzbuzz.convert(5) == "Buzz"


def test_3の倍数かつ5の倍数の場合でFizzBuzzを返す(fizzbuzz):
    assert fizzbuzz.convert(15) == "FizzBuzz"


def test_それ以外の場合はnを返す(fizzbuzz):
    assert fizzbuzz.convert(7) == "7"


def test_引数がint型でない場合にValueErrorを発生させる(fizzbuzz):
    with pytest.raises(ValueError) as e:
        fizzbuzz.convert("a")
    assert str(e.value) == "引数がint型ではありません。"

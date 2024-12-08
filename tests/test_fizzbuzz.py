import pytest
from src.fizzbuzz import FizzBuzz


@pytest.fixture
def fizzbuzz():
    fizzbuzz = FizzBuzz()
    return fizzbuzz


def test_fizzbuzz_3の倍数でFizzを返す(fizzbuzz):
    assert fizzbuzz.convert(3) == "Fizz"


def test_fizzbuzz_5の倍数でBuzzを返す(fizzbuzz):
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.convert(5) == "Buzz"


def test_fizzbuzz_3の倍数かつ5の倍数の場合でFizzBuzzを返す(fizzbuzz):
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.convert(15) == "FizzBuzz"


def test_fizzbuzz_それ以外の場合はnを返す(fizzbuzz):
    fizzbuzz = FizzBuzz()
    assert fizzbuzz.convert(7) == "7"


def test_fizzbuzz_引数がint型でない場合にValueErrorを発生させる(fizzbuzz):
    fizzbuzz = FizzBuzz()
    with pytest.raises(ValueError) as e:
        fizzbuzz.convert("a")

    assert str(e.value) == "引数がint型ではありません。"


# classを使う場合の書き方
class Test_3の倍数の場合:
    def test_3でFizzを返す(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.convert(3) == "Fizz"

    def test_6でFizzを返す(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.convert(6) == "Fizz"

    def test_9でFizzを返す(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.convert(9) == "Fizz"
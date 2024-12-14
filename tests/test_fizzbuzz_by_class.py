import pytest
from src.fizzbuzz import FizzBuzz


class FizzBuzzクラスの:

    class convertメソッドは:

        def 値が3の倍数の場合はFizzを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(3) == "Fizz"
    
        def 値が5の倍数の場合はBuzzを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(5) == "Buzz"
    
        def 値が3の倍数かつ5の倍数の場合はFizzBuzzを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(15) == "FizzBuzz"

        def それ以外の場合はnを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(7) == "7"

        def 引数がint型でない場合はValueErrorを発生させる(self):
            fizzbuzz = FizzBuzz()
            with pytest.raises(ValueError) as e:
                fizzbuzz.convert("a")
            assert str(e.value) == "引数がint型ではありません。"

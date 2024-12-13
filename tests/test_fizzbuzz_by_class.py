from src.fizzbuzz import FizzBuzz


class Test_FizzBuzzクラスの:

    class Test_convertメソッドについて:

        def test_3の倍数の場合はFizzを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(3) == "Fizz"
    
        def test_5の倍数の場合はBuzzを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(6) == "Fizz"
    
        def test_3の倍数かつ5の倍数の場合はFizzBuzzを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(9) == "Fizz"

        def test_それ以外の場合はnを返す(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(9) == "Fizz"

        def test_引数がint型でない場合はValueErrorを発生させる(self):
            fizzbuzz = FizzBuzz()
            assert fizzbuzz.convert(9) == "Fizz"


class FizzBuzz:

    def convert(self, n):
        """
        引数がint型でない場合にValueErrorを発生させる
        3の倍数の場合は「Fizz」,
        5の倍数の場合は「Buzz」,
        3の倍数かつ5の倍数の場合（すなわち15の倍数の場合）は「Fizz Buzz」,
        それ以外の場合は「n」を返却する
        # 引数がint型でない場合にValueErrorを発生させる
        """    
        if not isinstance(n, int):
            raise ValueError("引数がint型ではありません。")

        if (n % 3 == 0) and (n % 5 == 0):
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return str(n)
    
if __name__ == "__main__":
    fizzbuzz = FizzBuzz()
    print(fizzbuzz.convert(int(input())))

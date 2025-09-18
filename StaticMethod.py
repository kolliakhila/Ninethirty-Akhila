class NumberCheck:
    pass
    @staticmethod
    def is_even(num):
        if num%2==0:
            print(num,"is even")
        else:
            print(num,"is odd")
NumberCheck.is_even(10)

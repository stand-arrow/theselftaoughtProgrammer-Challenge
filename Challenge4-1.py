#１．数字を入力値として受け取り、その数字を2乗した戻り値を返す関数を書いてみよう


def square(x):
    """
    returns x ** 2
    :param
    :param
    :return 数字を２乗して返す
    """
    return x ** 2

number = int(input("input number;"))
y = square(number)
print(y)



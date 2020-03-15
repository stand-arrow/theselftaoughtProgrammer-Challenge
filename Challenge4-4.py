#４．２つの関数からなるプログラムを書いてみよう。1つ目の関数は整数を受け取り、その整数を２で割って求められる整数を出力として返そう。
#２つの目の関数は整数を引数として受け取り、４でかけた整数を返そう。
#プログラム内で、１つ目の関数を呼び、戻り値を変数として保存し、２つ目の関数の引数として渡そう。

def gethalfInteger(x):
    """
    Returns x / 2
    :param x:int
    :return 整数を２で割って整数を返す
    """
    return x / 2

def getFourTimesInteger(y):
    """
    Return y * 4
    :param y
    :return ４でかけた整数を返す
    """
    return y * 4

x = gethalfInteger(6)
y = getFourTimesInteger(x)

print(y)   

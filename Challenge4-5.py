#５．文字列をfloat型に変換して戻り値とする関数を書いてみよう。
#起こり得る例外をキャッチする例外処理を書こう。

def convertTofloat(x):
    """
    Reterns x
    :param x:String
    :return: convert String to float 
    """
    try:
        return float(x)
    except(ValueError):
        print("ERROR:Invalid Input")
        

print (convertTofloat("a"))

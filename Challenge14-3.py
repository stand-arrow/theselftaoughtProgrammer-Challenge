#３．２つのパラメーターを受け取る関数を書こう。
#この関数は同じオブジェクトを渡されたらTrueを返し、そうじゃなかったらFalseを返そう。

def isObject(obj1,obj2):
    """
        引数のオブジェクトを比較する
            param obj1:Object 比較元オブジェクト
            param obj2:Object 比較先オブジェクト
            return boolean
    """
    return obj1 is obj2

class Shape:
    def what_am_i(self):
        """
            "I am a shape"と文字列を返す
        """
        return "I am a shape"

shape1 = Shape()
shape1a = shape1
print(isObject(shape1,shape1a))

shape2 = Shape()
print(isObject(shape1,shape2))


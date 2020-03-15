#３．Shapeクラスを定義しよう。呼ばれたら"I am a shape"を返すメソッドwhat_am_iを定義しよう。
#前のRectangeとSquareクラスを変更して、このShapeクラスを継承させよう。
#そして、RectangeとSquareクラスのオブジェクトを生成して、このチャレンジで追加したメソッドwhat_am_iを呼んでみよう。

class Shape:
    def what_am_i(self):
        """
            "I am a shape"と文字列を返す
        """
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self, s1, s2, s3, s4):
        """
            param s1:float 辺１
            param s2:float 辺２
            param s3:float 辺３
            param s4:float 辺４
        """
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4

    def calculate_perimeter(self):
        """
            param self:Object 4辺それぞれの長さを格納しているオブジェクト
            return 外周の長さ
        """
        return self.side1 + self.side2 + self.side3 + self.side4

class Square(Shape):
    def __init__(self, s1, s2, s3, s4):
        """
        Square(正四角形)クラスの初期値
            param s1:float 辺１：上辺（幅）
            param s2:float 辺２：左辺（高さ）
            param s3:float 辺３：右辺（高さ）
            param s4:float 辺４:下辺（幅）
        """
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4

    def calculate_perimeter(self):
        """
            param self:Object 4辺それぞれの長さを格納しているオブジェクト
            return 外周の長さ
        """

        return self.side1 + self.side2 + self.side3 + self.side4

    def chamge_size(self, width):
        self.side1 += width
        self.side4 += width

own_rectangle = Rectangle(10,10,10, 10)
owm_square = Square(10, 10, 10, 10)
print (own_rectangle.what_am_i())
print (owm_square.what_am_i())

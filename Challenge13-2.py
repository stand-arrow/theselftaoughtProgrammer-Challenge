#２．Squareクラスにchamge_sizeメソッドを定義して、そこに渡した数値の分だけSquareオブジェクトの
#横幅を増やしたり、減らしたり（マイナス値の場合）してみよう。
class Square:
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


own_square = Square(10,10,10,10)
print (own_square.calculate_perimeter())
own_square.chamge_size(5)
print (own_square.calculate_perimeter())
own_square.chamge_size(-5)
print (own_square.calculate_perimeter())

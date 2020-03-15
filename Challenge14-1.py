#１．Squareクラスにsquare_listクラス変数を追加しよう。
#そして、新しくSquareクラスのオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう。

class Shape:
    def what_am_i(self):
        """
            "I am a shape"と文字列を返す
        """
        return "I am a shape"

class Square(Shape):
    square_list = []
    
    def __init__(self, s1, s2, s3, s4):
        """
        Square(正四角形)クラスの初期値とクラス変数を加える
            param s1:float 辺１：上辺（幅）
            param s2:float 辺２：左辺（高さ）
            param s3:float 辺３：右辺（高さ）
            param s4:float 辺４:下辺（幅）

        """
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.square_list.append(self)

    def calculate_perimeter(self):
        """
            param self:Object 4辺それぞれの長さを格納しているオブジェクト
            return 外周の長さ
        """
        return self.side1 + self.side2 + self.side3 + self.side4

    def chamge_size(self, width):
        self.side1 += width
        self.side4 += width

square1 = Square(10,20,30,40)
square2 = Square(2,3,4,5)
print(Square.square_list)

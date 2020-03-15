#２．Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さを出力しよう。
#たとえば、square(29)のようにオブジェクトを作ったら、print関数では29 by 29 by 29 by 29と出力しよう。
class Shape:
    def what_am_i(self):
        """
            "I am a shape"と文字列を返す
        """
        return "I am a shape"

class Square(Shape):
    square_list = []
    
    def __init__(self, size):
        """
        Square(正四角形)クラスの初期値とクラス変数を加える
            param size:float ：正方形の辺
        """
        self.side = size
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

    def calculate_perimeter(self):
        """
            param self:Object 正方形の辺の長さを格納しているオブジェクト
            return 外周の長さ
        """
        return self.side * 4

    def chamge_size(self, width):
        self.side += width

square1 = Square(29)
print(square1)

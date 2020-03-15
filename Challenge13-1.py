#１．RectangleとSquareクラスを作ろう。両方のクラスに、その図形の外周の長さを計算して返すcalculate_perimeterメソッドを定義しよう。
#そして、RectangleとSquareのオブジェクトを作って、それぞれのcalculate_perimeterメソッドを呼ぼう。

class Rectangle:
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
    
class Square:
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

Rresult = Rectangle(1,2,3,4)
Sresult = Square(10,20,30,40)
print(Rresult.calculate_perimeter())
print(Sresult.calculate_perimeter())

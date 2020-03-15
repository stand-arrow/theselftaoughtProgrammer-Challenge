#４．六角形を表すHexagonクラスを定義しよう。
#そのクラスには、外周の長さを計算して返すメソッドcalculate_perimeterを定義しよう。
#そして、Hexagonオブジェクトを作ってcalculate_perimeterメソッドを呼び出し、結果を出力しよう。

class Hexagon:
    def __init__(self,side1,side2,side3,side4,side5,side6):
        """
            param side1:float 辺１
            param side1:float 辺２
            param side1:float 辺３
            param side1:float 辺４
            param side1:float 辺５
            param side1:float 辺６
        """
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
        self.s4 = side4
        self.s5 = side5
        self.s6 = side6

    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

result = Hexagon(1, 2, 3, 4, 5, 6)
print(result.calculate_perimeter())

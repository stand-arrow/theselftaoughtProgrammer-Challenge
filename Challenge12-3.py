#３．三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。
#そしてTriangleオブジェクトを作って、areaメソッドを呼び出して、結果を出力しよう。

class Triangle:
    def __init__(self,b,h):
        """
            param bottom:float 底辺
            param height:float 高さ
        """
        self.bottom = b
        self.height = h

    def area(self):
        return (self.bottom * self.height) / 2

result = Triangle(10.5, 2)
print(result.area())

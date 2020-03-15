#１．りんごと言われて思い浮かぶ、４つの属性を考えよう。
#その４つの属性をインスタンス変数に持つ。Appleクラスを定義しよう。

class Apple:
    def __init__(self,weight,color,form,foodclass):
        """
            param weight:float グラム(g)
            param color:string 色
            param form:str 形
            param foodclass:str 食品分類
        """
        self.weight = weight
        self.color = color
        self.form = form
        self.foodclass = foodclass
        print("Apple created")


apple1 = Apple(100.5, "red", "ball", "fruit")
print(apple1.weight)
print(apple1.color)
print(apple1.form)
print(apple1.foodclass)
    

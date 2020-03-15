#４．HorseクラスとRiderクラスを定義しよう。
#コンポジションを使って、馬（Horse）に騎手(Rider)を持たせよう。

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.owner = rider

class Rider:
    def __init__(self, name):
        self.name = name

own_rider = Rider("tatsuya")
own_horse = Horse("sam", own_rider)

print (own_horse.owner.name)
    

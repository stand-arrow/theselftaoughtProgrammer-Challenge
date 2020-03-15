from random import shuffle

class Card:
    """
        カードクラス
        クラス変数：
            suits []：トランプの記号4種類（スペード、ハート、ダイアモンド、クラブ）を格納。格納順で記号間の強さも表している。
            　　　　弱さ順で格納されている。
            values []：トランプの全値を格納。弱さ順で格納されている。
        特殊メソッド：
            __init__()：初期化メソッド。引数の整数値でカードの記号と値を設定する。
            __lt__()："<"比較メソッド。引数のCardインスタンスの比較結果をbooleanで返す。
            __gt__()：">"比較メソッド。引数のCardインスタンスの比較結果をbooleanで返す。
            __repr__()："print"メソッド。引数のCardインスタンスをもとに「"values[value]" of "suits[suit]"」の文字列を返す。 
    """
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        """
            インスタンス変数： 
                value int：トランプの値を索引するインデックス値
                suit int：トランプの記号を索引するインデックス値
        """
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
        return False
    
    def __repr__(self):
        v = self.values[self.value] +  " of " \
            + self.suits[self.suit]
        return v

class Deck:
    """
        デッキクラス
        特殊メソッド：
            __init__：初期化メソッド。シャッフルしたトランプ一式のカードを用意する。
        メソッド：
            rm_card：末尾のカードを取り出す。
    """
    def __init__(self):
        """
            インスタンス変数：
                cards []：デッキ。シャッフルしたトランプ一式。
        """
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    """
        プレイヤークラス
        特殊メソッド：
            __init__：初期化メソッド。プレイヤーの初期設定を行う。
    """
    def __init__(self, name):
        """
            インスタンス変数：
            wins int:プレイヤーの勝利数
            card Card：プレイヤーが持っているカード
            name str：プレイヤー名
        """
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    """
        ゲームクラス
        特殊メソッド：
            __init__：初期化メソッド。デッキ準備とプレイヤー２人の名前を入力する。
        メソッド：
            wins：ラウンドの勝利プレイヤーを出力する
            draw：プレイヤー１とプレイヤー２が引いたカードを出力する
            play_game；戦争ゲームの進行を行う
            winner：戦争ゲームの勝利プレイヤーを判定する
    """
    def __init__(self):
        """
            インスタンス変数：
            deck Deck:デッキ
            p1 Player：プレイヤー１
            p2 Player：プレイヤー２
        """
        name1 = input("プレーヤー１の名前 ")
        name2 = input("プレーヤー２の名前 ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def wins(self, winner):
        print("このラウンドは{}が勝ちました".format(winner))
    
    def draw(self, p1, p2):
        print("{}は{},{}は{}を引きました".format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます")
        while len(cards) >= 2:
            m = "qで終了、それ以外のキーでplay:"
            response = input(m)
            if response == 'q':
                break
            self.p1.card = self.deck.rm_card()
            self.p2.card = self.deck.rm_card()
            self.draw(self.p1, self.p2)
            if self.p1.card > self.p2.card:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        
        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{}の勝利です!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け"

game = Game()
game.play_game()


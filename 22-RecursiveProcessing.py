#再帰処理
#再帰法のルール
#再帰終了条件を持つ
#状態を変えながら再帰終了条件に進む
#再帰的に関数自身を呼び出す

def bottles_of_beer(bob):
    """ Prints Bottle of Beer on the Wall lyrics.

    :param bob: Must be a positive integer.
    """
    if bob < 1:
        print("""No more bottles of beer on the wall.No more bottles of beer.""")
        return
    
    tmp = bob
    bob -= 1
    print("""{} bottles beer on the wall.
        {} bottles of beer.
        Take one down, pass it around,
        {} bottles of beer on the wall.
        """.format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(10)
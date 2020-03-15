#４．無限ループする数字当てプログラムを書こう。
#ユーザーに文字を入力してもらう。qが入力されたら終了。数字が入力されたら正解か判定する。
#正解の数はプログラム内にいくつかリストで持たせておく。
#ユーザーが入力した数字がいずれかと一致したら「正解」、一致しなかったら「不正解」と表示する。
#数字かq以外が入力されたら「数字を入力するか、qで終了します」と表示しよう
anserNumbers = [1,5,9]

while True:
    inputAnswer = input("適当な文字を入力してください；")
    if inputAnswer == "q":
        break
    try:
        inputAnswer = int(inputAnswer)
    except ValueError:
        print("数字を入力するか、qで終了します")
        continue
    if inputAnswer in anserNumbers:
        print("正解")
    else:
        print("不正解")

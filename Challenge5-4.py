#４．任意のキーを入力させるプログラムを書こう。
#入力されたキーを使って、1つ前のチャレンジで用意した辞書から、バリューを取得して表示しよう。

myprofile = {
    "身長":"171cm",
    "好きなミュージシャン":"ポルノグラフィティ",
    "年齢":"33歳",
    "体重":"56.1kg",
    "血液型":"AB",
    "出身県":"福井県"
    }

attribute = input("見たいプロフィール項目を入力してください。（身長、年齢、体重、血液型、出身県、好きなミュージシャン）")

print (myprofile[attribute])

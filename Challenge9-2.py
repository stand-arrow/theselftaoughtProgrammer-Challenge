#２．何か質問するプログラムを書こう。入力された回答をファイルに書き出そう。
answer = input("好きな色は？：")

with open("color.txt","w",encoding="UTF-8") as fs:
    fs.write(answer)


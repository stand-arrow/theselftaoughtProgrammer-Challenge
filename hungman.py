"""
ハングマンゲーム
Chapter10,
Chapter10 Challenge1
"""
import random

def hungman(word):
    """
    ハングマンゲームを実行する
    param word:string
    """

    wrong = 0
    stages = ["",
            "____________        ",
            "|         |         ",
            "|         |         ",
            "|         O         ",
            "|        -|-        ",
            "|        」L        ",
            "|                   "
            ]
    board = ["_"] * len(word)
    wordlist = list(word)
    win = False
    print("ハングマンゲームへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        char = input("1文字入れてください：")
        if char in wordlist:
            cindex = wordlist.index(char)
            board[cindex] = char
            wordlist[cindex] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        end = wrong + 1
        print("\r\n".join(stages[0:end]))
        if "_" not in board:
            print("勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\r\n".join(stages[0:wrong + 1]))
        print("負け！正解は{}".format(word))

words = ["cat","dog","bird","mouse","snake"]

hungman(random.choice(words))


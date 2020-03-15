#１．コンピューターにある何かのファイルをPythonで開いて、コンテンツを出力しよう。
import os

filepath = os.path.join("C:\\","Users","dolph","OneDrive","ドキュメント","hellowworld.txt")
with open(filepath,"r") as f:
    print(f.read())

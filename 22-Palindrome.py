#回文チェック

def palindrome(word):
    word = word.lower()
    return word[::-1] == word #[::-1]はシーケンス全体のスライスを逆順で返す

print(palindrome("Mother"))
print(palindrome("Mam"))
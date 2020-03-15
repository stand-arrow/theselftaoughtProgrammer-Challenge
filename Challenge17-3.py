#３．Pythonの re モジュールを使って、何かの文字の後に o が2回登場する単語に一致する正規表現を加工。
# そして、"The ghost that says boo haunts the loo" の文中にあるbooやlooに一致するか試そう
import re

line = "The ghost that says boo haunts the loo"
m = re.findall(".oo", line)
print(m)
#３．リストのリストに含まれている要素をCSVファイルに書き出そう。
#データ：
#[["Top Gun", "Risky Business", "Minority Report"],
#["Titanic", "The Revenant", "Inception"],
#["Training Day", "Man on Fire", "Flight"]]
#データの各要素はCSVの１行となり、その１行に含まれる各要素がカンマで区切られるように書き出そう。
import csv

cinemas = [["Top Gun", "Risky Business", "Minority Report"],
           ["Titanic", "The Revenant", "Inception"],
           ["Training Day", "Man on Fire", "Flight"]]

with open("cinems_list.csv","w",encoding="UTF-8",newline='') as fs:
    fc = csv.writer(fs, delimiter=",")
    for cinema in cinemas:
        fc.writerow(cinema)
        

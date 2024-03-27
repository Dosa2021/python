# st = open("st.txt", "w")
# st.write("Hi")
# st.close()

# # with分を使うことで、処理が終わると自動でcloseする
# with open("st.txt", "w") as f:
#     f.write("永野芽郁様、、")

# # ファイル読みこみ
# with open("st.txt", "r") as f:
#     print(f.read())


# fileを読み込んでリストに入れる
# my_list = []

# with open("st.txt", "r") as f:
#     my_list.append(f.read())

# print(my_list)

import csv

# csv書き込み
with open("st.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])

# csv読み込み
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

# 独学プログラマー「9. ファイル」完

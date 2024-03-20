#--------------------------------------------------
# 10. 文字の連結
# name = 'たつや'
# age = 10

# # ①
# print(name + str(age) + '歳だよ')

# # ②
# print('{} {} 歳だよ'.format(name, age))

# # ③
# print(f'{name}{age}歳だよ')

#--------------------------------------------------
# 11. ユーザからの入力を受け取る
# num = input("Number? ")
# # print(int(num))
# print(float(num)) # 浮動小数点

# #--------------------------------------------------
# # 12. f文字列のオプション

# initial_balance = int(input("initial balance? "))
# RATE = 1.1

# # ,区切りになる
# print(f"Year: 0 {initial_balance:,}")

# # 小数点1000.00の表記
# print(f"Year: 1 {initial_balance * RATE:.2f}")
# print(f"Year: 2 {initial_balance * RATE * RATE:,.2f}")

#--------------------------------------------------
# 13. if
# 特になし

#--------------------------------------------------
# 14. if else
# 特になし

#--------------------------------------------------
# 15. 論理演算子
# if not

#--------------------------------------------------
# # 16. elif
# # 17. match

signal = input("Signal color? ")

# # if signal == "red":
# #     print("Stop!!!!----------")
# # elif signal == "yell":
# #     print("Slow down!-----")
# # elif signal == "blue" or signal == "green":
# #     print("Go-----")
# # else:
# #     print("Invalid color")

# # python3.10の機能らしい。。。
match signal:
    case "red":
        print("Stop!!!!----!!!!!")
    case "yellow":
        print("Slow down!")
    case "blue" | "green":
        print("Go!")
    case _:
        print("Invalid signal color...")

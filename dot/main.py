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

# signal = input("Signal color? ")

# # # if signal == "red":
# # #     print("Stop!!!!----------")
# # # elif signal == "yell":
# # #     print("Slow down!-----")
# # # elif signal == "blue" or signal == "green":
# # #     print("Go-----")
# # # else:
# # #     print("Invalid color")

# # # python3.10の機能らしい。。。
# match signal:
#     case "red":
#         print("Stop!!!!----!!!!!")
#     case "yellow":
#         print("Slow down!")
#     case "blue" | "green":
#         print("Go!")
#     case _:
#         print("Invalid signal color...")

#--------------------------------------------------
# 18. if else を一行で
# initial_balance = 20_000
# # if float(initial_balance) >= 100000:
# #     RATE = 1.1
# # else:
# #     RATE = 1.01

# # 上と同じ意味
# RATE = 1.1 if initial_balance >= 100_000 else 1.01

# print(f"Current rate: {RATE:.2f}")
# print(f"Year 0: {initial_balance:,.2f}")
# print(f"Year 1: {initial_balance * RATE:,.2f}")

#--------------------------------------------------
# 19 match と if
# initial_balance = 80_000
# # if float(initial_balance) >= 100_000:
# #     RATE = 1.1
# # elif float(initial_balance) >= 80_000:
# #     RATE = 1.08
# # elif float(initial_balance) >= 60_000:
# #     RATE = 1.06
# # else:
# #     RATE = 1.01

# match initial_balance:
#     case n if n >= 100_000:
#         RATE = 1.1
#     case n if n >= 80_000:
#         RATE = 1.08
#     case n if n >= 60_000:
#         RATE = 1.06
#     case _:
#         RATE = 1.01
# print(f"Current rate: {RATE:.2f}")
# print(f"Year 0: {initial_balance:,.2f}")
# print(f"Year 1: {initial_balance * RATE:,.2f}")


#--------------------------------------------------
# 20 反復処理

# for
# for i in range(10):
# for i in range(3, 9):
# for i in range(3, 9, 2): # 3, 5, 7
# for i in range(8, 5, -1): # 8, 7, 6
#     print(f"{i} hello")

#--------------------------------------------------
# 21 forとf文字列

initial_balance = 100_000
RATE = 1.1
# print(f"Year 0: {initial_balance * RATE ** 0:,.2f}")
# print(f"Year 1: {initial_balance * RATE ** 1:,.2f}")
# print(f"Year 2: {initial_balance * RATE ** 2:,.2f}")

# 上と同じ意味
for i in range(3):
    print(f"Year {i}: {initial_balance * RATE ** i:,.2f}")

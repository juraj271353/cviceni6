# def basic_stats(values):
#     return min(values), max(values), round(sum(values) / len(values), 2)
#
#
# return_var = basic_stats([1200, 980, 1430, 1600, 890])
# print(return_var)
#
# min_v, max_v, avg_v = basic_stats([1200, 980, 1430, 1600, 890])
# print(min_v, max_v, avg_v)
#
#
# avg_only = basic_stats([1200, 980, 1430, 1600, 890])[2]
# print(avg_only)


# def local_demo():
#     value = "local"
#     print("uvnitř funkce:", value)
#
#
# local_demo()
# print(value)  # NameError: value mimo funkci neexistuje


# DEFAULT_ROUND = 2
#
#
# def round_value(value):
#     return round(value, DEFAULT_ROUND)
#
#
# print(round_value(12.3456))  # 12.35


# player_name = "GlobalPlayer"
#
#
# def show_player():
#     player_name = "LocalPlayer"
#     print("ve funkci:", player_name)
#
#
# show_player()
# print("mimo funkci:", player_name)


# counter = 10
#
#
# def increment_bad():
#     # Python to chápe jako lokální proměnnou `counter`,
#     # takže řádek níže spadne na UnboundLocalError.
#     counter = counter + 1
#     return counter
#
# print(increment_bad())


# counter = 10
#
#
# def increment_global():
#     global counter
#     counter = counter + 1
#     return counter
#
#
# print(increment_global())  # 11
# print(counter)             # 11


import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [3, 1, 4])
plt.show()
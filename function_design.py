from curses.ascii import isdigit, isupper

SPECIAL_SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"

def analyze_password(
    password,
    min_length = 8,
    require_digit = True,
    require_upper = True,
    require_symbol = False,
    banned_words = None,
):



    if len(password) != min_length:
        print("Nie je dodrzana minimalna dlzka.")

    if require_digit:
        if isdigit(password):
            continue
        else:
            print("Neobsahuje cislicu.")

    if require_upper:
        if isupper(password):
            continue
        else:
            print("Neobsahuje velke pismeno.")

    if require_symbol:
        has_special = any([ch in SPECIAL_SYMBOLS for ch in password])
        print(has_special)

    for ch in password:
        if ch in banned_words:
            print("Obsahuje zakazany znak.")
from __future__ import annotations


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))


def can_buy_alcohol(age: int) -> bool | None:
    if type(age) != int:
        return

    if age >= 18:
        return True
    else:
        return False


print(can_buy_alcohol(28))
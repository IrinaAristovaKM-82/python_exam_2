
"""
    Написати валідатор ....
    Правило валідації
"""

import re

def getUserID():

    user_input = input("Enter ID:\n")

    if (re.match(r"^\d{16}", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
"""

def getBankName():
    user_input = input("Enter your bank name:\n")
    if (re.match(r"[A-Z]\w+\d*", user_input)):
        return user_input
    else:
        return



"""
    Написати валідатор ....
    Правило валідації
"""


def getBankCredit():
    user_input = input("Enter credit:\n")
    if (re.match(r"^\d{4}\.\d", user_input)):
       return user_input
    else:
        return False
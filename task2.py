from data import dataset

from validators.lib import getUserID
from validators.lib import getBankName
from validators.lib import getBankCredit

from task1 import addUserID

def addUserIDValidator():
    user_id = getUserID()
    while not user_id:
        print("Error in id. Try again")
        user_id = getUserID()
    bank = getBankName()
    while not bank:
        print("Error in bank. Try again")
        bank = getBankName()
    credit = getBankCredit()
    while not credit:
        print("Error in credit. Try again")
        credit = getBankCredit()
    credit = float (credit)
    addUserID(user_id, bank, credit)

print("Task 2")

addUserIDValidator()

print(dataset)

print("\n\n")
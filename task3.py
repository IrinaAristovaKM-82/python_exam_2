from data import dataset
from task1 import *


def recursionByBank(id, bank, credit = 0):
    if bank==[]:
        return credit
    bank = dataset[id][bank[0]]
    credit = sum(bank)
    return recursionByBank(id, bank[1:], credit)


def recursionByID(id=list(dataset.keys()), result_dict=dict()):
    if id == []:
        return result_dict
    id = id[0]
    bank_list = list(dataset[id].keys())
    credit = recursionByBank(id, bank_list)
    result_dict[id] = credit
    return recursionByID(id[1:], result_dict)

print("Task 3")

result = recursionByID()
print(result)

print("\n\n")




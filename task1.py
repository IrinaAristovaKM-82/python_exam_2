from data import dataset

def addUserID(ID, bank, credit):
    if ID in dataset:
        if bank in dataset[ID]:
            bank_list = dataset[ID][bank]
            bank_list.append(credit)
        else:
            dataset[ID][bank] = [credit]
    else:
        dataset[ID] = {bank: [credit]}

print("Task 1")

addUserID("1234512345123456", "Privar24", "(1121.0грн)")

print(dataset)


print("\n\n")
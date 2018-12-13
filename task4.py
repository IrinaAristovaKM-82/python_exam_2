from data import dataset
from task1 import *
import plotly

import plotly.graph_objs as go
data = dict()

def sumbank(result, bank_list):
    result += 0.0
    for item in bank_list:
        result += float(item[1:-4])
        return result

for ID in list(dataset.keys()):
    for bank, bank_list in (dataset[ID]).items():
        if ID in data:
            data[ID] += sum(bank_list)
        else:
            data[ID] = sum(bank_list)
print(data)

diagram = go.Bar(
    x=list(data.keys()),
    y=list(data.values())
)

fig = go.Figure(data=[diagram])

plotly.offline.plot(fig, filename='user expenses.html')
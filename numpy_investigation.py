import numpy as np
import plotly.graph_objects as go


numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

np.random.shuffle(numbers)

print (numbers)

fig = go.Figure(data=[go.Bar(x=np.arange(len(numbers)), y=numbers)])


fig.show()


input("press any key to end")
import matplotlib.pyplot as plt
import pandas as pd

heights = pd.read_csv('average-height-of-men-for-selected-countries.csv')

peru_heights = heights[heights['Entity'] == 'Peru']
peru_heights.columns = ['Entity','Code','Year','Heights']
peru_heights.plt.plot(x = 'Entity',y = 'Heights',kind = 'line')


import pandas as pd
import matplotlib.pyplot as plt

heights = pd.read_csv('average-height-of-men-for-selected-countries.csv')

peru_heights = heights[heights['Entity'] == 'Peru']
peru_heights.columns = ['Entity','Code','Year','Heights']
peru_heights.plot(x = 'Entity',y = 'Heights',kind = 'scatter')

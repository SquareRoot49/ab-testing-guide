import pandas as pd
import numpy as np

item = 'CY.CZC'
filename = item + '.h5'
data = pd.read_hdf('MarketDay/' + filename, header = None)
print(data)
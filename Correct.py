import pandas as pd

def fill_data(data):
    bag = []
    cp_date = data.copy()
    for date in cp_date['DATE'].unique():
        cp_date['DATE'] = pd.to_datetime(cp_date['DATE'])
        sec_dat = cp_date[cp_date['DATE'].dt.date == date]
        sec_dat["CLOSE"] = sec_dat["CLOSE"].fillna(sec_dat["CLOSE"].mean())
        bag.append(sec_dat)
    Data_cp = pd.concat(bag)
    data['CLOSE'] = Data_cp['CLOSE']
    return data
if item == 'CY':
    data = pd.read_hdf('MarketDay/' + filename, header = None)
    Data = fill_data(data)
else:
    Data = pd.read_hdf('MarketDay/' + filename, header = None)

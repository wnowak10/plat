# import data

import quandl
import pandas as pd
from key import auth_key

#### LOAD FINANCE DATA ####

start="2015-1-1"
end="2017-1-1"
plat = quandl.get("LPPM/PLAT", start_date=start, end_date=end,authtoken=auth_key)['USD AM']
sp= quandl.get("YAHOO/INDEX_GSPC", start_date=start, end_date=end,authtoken=auth_key)['Adjusted Close']
tif  = quandl.get("WIKI/TIF", start_date=start, end_date=end,authtoken=auth_key)['Adj. Close']

features = pd.concat([tif, sp,plat], axis=1)
features.columns=['tif_stock','sp_500','plat']
# drop missing platinum values
features=features.dropna(axis=0,subset=['plat'])
# create target..for today, we have yesterday minute today
movement = features.plat.shift(-1)-features.plat

# compile into one df for kicks
all_data=pd.concat([features,movement],axis=1)
all_data.columns=['tif_stock','sp_500','plat_today','movement']
all_data['gain_loss'] = [1 if x>0 else 0 for x in all_data['movement']]
# remove most current row, because we dont know what tomorrow's
	# plat price will be...so let's get rid of this
all_data=all_data[:-1:]
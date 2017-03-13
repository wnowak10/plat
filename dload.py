# import data

import quandl
import pandas as pd
from key import auth_key

#### LOAD FINANCE DATA ####

start="2015-1-1"
end="2017-1-1"

# API calls to quandl
plat = quandl.get("LPPM/PLAT", start_date=start, end_date=end,authtoken=auth_key)['USD AM']
sp= quandl.get("YAHOO/INDEX_GSPC", start_date=start, end_date=end,authtoken=auth_key)['Adjusted Close']
tif  = quandl.get("WIKI/TIF", start_date=start, end_date=end,authtoken=auth_key)['Adj. Close']
oil=quandl.get("OPEC/ORB", start_date=start, end_date=end,authtoken=auth_key)['Value']
gold=quandl.get("BUNDESBANK/BBK01_WT5511", start_date=start, end_date=end,authtoken=auth_key)['Value']
silver=quandl.get("LBMA/SILVER", start_date=start, end_date=end,authtoken=auth_key)['USD']
bitcoin=quandl.get("BAVERAGE/USD", start_date=start, end_date=end,authtoken=auth_key)['Last']

#rename columns
fin_names=[	'sp_500',
			'tif_stock',
			'oil','gold',
			'silver',
			'bitcoin',
			'plat']
# build pd df
features = pd.concat([sp,tif,oil,gold,silver,bitcoin,plat], axis=1)
features.columns=fin_names

# drop missing platinum values
features=features.dropna(axis=0,subset=['plat'])

# create target variable...for today, we have yesterday minus today
movement = features.plat.shift(-1)-features.plat

# compile into one df for kicks
all_data=pd.concat([features,movement],axis=1)
new_names=fin_names.append('movement')
all_data.columns=fin_names

# create gain_loss -- predict next day's gain or loss
all_data['gain_loss'] = [1 if x>0 else 0 for x in all_data['movement']]


# remove most current row, because we dont know what tomorrow's
	# plat price will be...so let's get rid of this
all_data=all_data[:-1:]
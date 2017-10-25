from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)

kw_list = ["netflix"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')

import seaborn as sns
import matplotlib.pyplot as plt

plt.plot(pytrends.interest_over_time()['netflix'])
plt.title('netflix over time. love - bill')
plt.show()
# for creation of special candles

from datetime import datetime as dt
import pandas as pd


def create_c():
     d = {'Open': [43, 50, 60, 70, 80, 95, 90],
          'High': [41, 50, 60, 70, 80, 96, 90],
          'Low': [50, 60, 70, 80, 90, 80, 80],
          'Close': [50, 60, 70, 80, 90, 90, 80]}
     df = pd.DataFrame(data=d, index=[dt.fromisoformat("2020-08-20"),
                                      dt.fromisoformat("2020-08-21"),
                                      dt.fromisoformat("2020-08-22"),
                                      dt.fromisoformat("2020-08-23"),
                                      dt.fromisoformat("2020-08-24"),
                                      dt.fromisoformat("2020-08-25"),
                                      dt.fromisoformat("2020-08-26")])
     return df


create_c()

# add hanging man

#                                 Open        High         Low       Close
#Datetime
#2021-09-01 14:03:00-04:00  303.309998  303.320007  303.260010  303.274994
#2021-09-01 14:04:00-04:00  303.269989  303.290009  303.260010  303.274994
#2021-09-01 14:05:00-04:00  303.260010  303.260010  303.000000  303.100006
#2021-09-01 14:06:00-04:00  303.089996  303.103912  303.049988  303.053314
#2021-09-01 14:07:00-04:00  303.059998  303.140015  303.049988  303.139801
#2021-09-01 14:08:00-04:00  303.130005  303.170013  303.107513  303.119995
#2021-09-01 14:09:00-04:00  303.126007  303.126007  303.041107  303.049988
#2021-09-01 14:10:00-04:00  303.059998  303.100006  303.049988  303.079987
#2021-09-01 14:11:00-04:00  303.059998  303.119995  303.059998  303.100006
#2021-09-01 14:12:00-04:00  303.100006  303.109985  303.054993  303.070007
#2021-09-01 14:13:00-04:00  303.059998  303.114990  303.059998  303.100006
#2021-09-01 14:14:00-04:00  303.100006  303.220001  303.089996  303.161011
#2021-09-01 14:15:00-04:00  303.179993  303.220001  303.160095  303.160614
#2021-09-01 14:16:00-04:00  303.160004  303.170013  303.149994  303.170013
#2021-09-01 14:17:00-04:00  303.160004  303.190002  303.160004  303.174988
#2021-09-01 14:18:00-04:00  303.170013  303.211792  303.170013  303.209991
#2021-09-01 14:19:00-04:00  303.200012  303.220093  303.200012  303.209991
#2021-09-01 14:20:00-04:00  303.220001  303.269989  303.210114  303.255005
#2021-09-01 14:21:00-04:00  303.255005  303.255005  303.154999  303.170013
#2021-09-01 14:22:00-04:00  303.149994  303.149994  303.070007  303.123901#

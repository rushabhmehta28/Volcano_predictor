
# stdlib imports
from datetime import datetime
import pandas as pd
from libcomcat.dataframes import get_summary_data_frame, get_detail_data_frame, get_magnitude_data_frame
from libcomcat.search import search, get_event_by_id

earthquake = search(starttime=datetime(2017, 1, 1, 00, 00),
                    endtime=datetime(2019, 1, 1, 00, 00),
                    minmagnitude=2.5,
                    orderby='time')

elist = []

for event in earthquake:
    temp = event.toDict()
    temp.update({"magType":event['magType']})
    elist.append(temp)

earthquake = pd.DataFrame(elist)
earthquake.drop(["url", "alert", "significance"], axis=1, inplace=True)

earthquake.to_csv("E:\Education\RWTHAachenUniversity\SS2021\TechLabs\quake_pull.csv")


#anaconda datapull command
#python C:\Users\andre\PycharmProjects\pythonProject\venv\Scripts\Techlabs\techlabs_datapull.py

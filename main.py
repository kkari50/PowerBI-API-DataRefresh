"""
Author: Krish Kari
Email: kkari@bislicer.com
website: https://www.bislicer.com/

This program refreshed individual dataflow and datasets respecrtively. This code can be scaled to
refresh all required dataflows and datasets based on enterd in [config.ini] file.
Please contact kkari@bislicer.com if you have any questions.
"""






from engine import *
from DataRefresh import *

dataflow_id = config['InputDetails']['dataflow_id']
dataset_id = config['InputDetails']['dataset_id']
group_id = config['InputDetails']['group_id']


access_token = get_access_token(config)


#---------Refresh dataset-------------#

refresh_dataset(dataset_id,access_token)

#---------Refresh datflow-------------#

refresh_dataflow(group_id=group_id, dataflow_id=dataflow_id, access_token=access_token)


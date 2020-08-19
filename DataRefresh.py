from config_parser import *



def refresh_dataset(dataset_id, access_token):
    url = config['APIs']['refresh_dataset_api'] +f'/{dataset_id}/refreshes'
    header = {'Authorization': f'Bearer {access_token}'}
    body = {'notifyOption': 'MailOnCompletion'}
    r = requests.post(url=url, headers=header, data=body)
    r.raise_for_status()

def refresh_dataflow(group_id,dataflow_id,access_token):
    url = config['APIs']['get_groups_api'] + f'/{group_id}/dataflows/{dataflow_id}/refreshes'
    header = {'Authorization': f'Bearer {access_token}'}
    body = {'notifyOption': 'MailOnCompletion'}
    r = requests.post(url=url, headers=header, data=body)
    r.raise_for_status()




# refresh_dataset(123)

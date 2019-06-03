# 1) request the file and output to the terminal on the right
# 2) parse the data into a structured format
# 3) add error handling

import requests

url = 'https://grahamgilbert.com/temp/interview.json'
response = requests.get(url)

def get_json(passed_id):
    if response.status_code == 200:
        json_data = response.json()
        for i in range(len(json_data)):
            id_data = json_data[i]

            if id_data['id'] == passed_id:
                ret = 'ID: ' + str(id_data['id']) 
                if 'device_checked_in' in id_data:
                    ret = ret + ' DEVICE CHECKED IN: ' + str(id_data['device_checked_in'])
                if 'assigned_user' in id_data:
                    ret = ret + ' USER: ' + id_data['assigned_user']
                return ret
            
        return 'Not found'
    else:
        return None
    
data = get_json(26)
print(data)
data = get_json(57)
print(data)
data = get_json(123)
print(data)



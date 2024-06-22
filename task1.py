import requests
import json

# GET request for fetching data from api endpoint
def get_data(url):
    response = requests.get(url)
    if response.status_code==200:
        print(type(response.json()))
        return response.json()
    else:
        print('Could not fetch data from API')

# Filtering method
def print_data(data):
    for item in data:
        if item['userId']>9:
            print(item)

# POST request for posting data to api endpoint
def post_data(url,payload):
    response = requests.post(url,data=payload)
    if response.status_code==201:
        print(f'Data posted successfluy with status code:{response.status_code}')

if __name__=='__main__':
    url='https://jsonplaceholder.typicode.com/posts'

    answer= input('Do you want to get data?')
    if answer== 'yes':
        id = input('Enter id:')
        get_url=f'{url}/{id}'
        data = get_data(get_url)
        print(data)

    answer= input('Do you want to post data?')
    if answer== 'yes':
        userId = input('Enter userId:')
        id = input('Enter id:')
        body = input('Enter body:')
        payload={'userId':{userId},'id':{id},'body':{body}}
        post_data(url,payload)
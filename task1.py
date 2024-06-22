import requests
import json


def get_data(url):
    response = requests.get(url)
    if response.status_code==200:
        print(type(response.json()))
        return response.json()
    else:
        print('Could not fetch data from API')

if __name__=='__main__':
    url='https://jsonplaceholder.typicode.com/posts'

    answer= input('Do you want to get data?')
    if answer== 'yes':
        id = input('Enter id:')
        get_url=f'{url}/{id}'
        data = get_data(get_url)
        print(data)
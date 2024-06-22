import requests
import json

# GET request for fetching data from api endpoint
def get_data(url):
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        print('Could not fetch data from API')

# Filtering method
def filter_data(data):
    for item in data:
        if item['userId']>9:
            print(item)

# POST request for posting data to api endpoint
def post_data(url,payload):
    response = requests.post(url,data=payload)
    if response.status_code==201:
        print(f'Post is created successfuly with status code:{response.status_code}')
    else:
        print(f'Post creation is unsuccessful with status code:{response.status_code}')
        print(f'Response Conetnt:{response.content}')

def update_data(url,payload):
    response = requests.put(url,data=payload)
    if response.status_code==200:
        print(f'Post is updated successfluy with status code:{response.status_code}')
        print(f'Updated Post:{response.json()}')
    else:
        print(f'Post updation is unsuccessful with status code:{response.status_code}')
        print(f'Response Conetnt:{response.content}')

def delete_data(url):
    response = requests.delete(url)
    if response.status_code==200:
        print(f'Post is deleted successfluy with status code:{response.status_code}')
    else:
        print('Could not delete post')

if __name__=='__main__':
    base_url='https://jsonplaceholder.typicode.com/posts'

    print('Select any one option')
    print('1: Read Post' '\n' 
          '2. Create Post' '\n'
          '3. Update Post' '\n'
          '2. Delete Post' '\n')
    answer= input('Select number:')
    if answer== '1':
        id = input('Enter id:')
        get_url=f'{base_url}/{id}'
        data = get_data(get_url)
        print(data)

    elif answer== '2':
        id = input('Enter id:')
        title = input('Enter title:')
        body = input('Enter body:')
        userId = input('Enter userId:')
        payload={'id':{id},'title':{title} ,'body':{body}, 'userId':{userId}}
        post_data(base_url,payload)

    elif answer== '3':
        id = input('Enter id:')
        title = input('Enter title:')
        body = input('Enter body:')
        userId = input('Enter userId:')
        payload={'id':{id},'title':{title} ,'body':{body}, 'userId':{userId}}
        update_url=f'{base_url}/{id}'
        update_data(update_url,payload)

    elif answer== '4':
        id = input('Enter id:')
        delete_url=f'{base_url}/{id}'
        delete_data(delete_url)
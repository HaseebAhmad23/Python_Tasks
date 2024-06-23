import requests
import json

# GET request method for fetching data
def get_data(url):
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.json()
        else:
            print('Could not fetch data from API')
    except requests.exceptions.RequestException as e:
        print(f'An error occured:{e}')

# Filtering method
def filter_data(data):
    for item in data:
        if item['userId']>9:
            print(item)

# POST request method for posting data
def post_data(url,payload):
    try:
        response = requests.post(url,data=payload)
        if response.status_code==201:
            print(f'Post is created successfuly')
        else:
            print(f'Post creation is unsuccessful')
            print(f'Response Conetnt:{response.content}')
    except requests.exceptions.RequestException as e:
        print(f'An error occured:{e}')

# PUT request method for updating data
def update_data(url,payload):
    try:
        response = requests.put(url,data=payload)
        if response.status_code==200:
            print(f'Post is updated successfluy')
            print(f'Updated Post:{response.json()}')
        else:
            print(f'Post updation is unsuccessful')
            print(f'Response Conetnt:{response.content}')
    except requests.exceptions.RequestException as e:
        print(f'An error occured:{e}')

# DELETE request method for deleting data
def delete_data(url):
    try:
        response = requests.delete(url)
        if response.status_code==200:
            print(f'Post is deleted successfluy')
        else:
            print('Post deletion is unsuccessful')
            print(f'Response Conetnt:{response.content}')
    except requests.exceptions.RequestException as e:
        print(f'An error occured:{e}')

if __name__=='__main__':
    base_url='https://jsonplaceholder.typicode.com/posts'

    print('Select any one option:' '\n'
          '1: Read Post' '\n' 
          '2. Create Post' '\n'
          '3. Update Post' '\n'
          '4. Delete Post' '\n')
    answer= input('Enter number:')

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

    else:
        print('Wrong input value')
        print('.... Exiting ....')
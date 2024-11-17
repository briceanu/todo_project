import requests
import sys


# admin user
# gigi  ak471989

# costica4 awdawd283AWD
# e295660f-7d6d-4a0b-895d-4407b1e8b14f


# marian123 awdawd283AWDawd
#  marian8888
# 4f77d9bc-a248-4f3d-9c33-6c9f09c0ab10
#  new password awdawd283AWDawdsef

# marian1234 awdawd283AWDawdadwd
def get_all_todos():

    url = 'http://localhost:8000/todos/all_todos'
    headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODYyMDg0LCJpYXQiOjE3MzE4NTg0ODQsImp0aSI6IjVhOTgzZDc4ZTNlNjRhNzI4OThlM2E5ZWI4NjBhZjhmIiwidXNlcm5hbWUiOiJtYXJpYW4xMjM0NTYifQ.boCsgp2odgUwD4qtq0myUetUcxRFvBTWnOLakrRzCKs'
            }


    res = requests.get(url=url,headers=headers)

    print(res.status_code)
    print(res.text)

 
def create_todo():

   url = 'http://localhost:8000/todos/create_todo'
#    token of marianmarian
   headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODAzODY4LCJpYXQiOjE3MzE4MDAyNjgsImp0aSI6ImE1NmNiMjYyMjI3NDRjMWFiN2FiNGFjMjkxNTUyODRmIiwidXNlcm5hbWUiOiJtYXJpYW5tYXJpYW4ifQ.Ocdy9BTFClGdgTLYVEZEUSsBUvmK6iqCVETV5WL84Fw'
            }
   data = {'task':'clean the cat marian mrian','completed':True}
#    data = {}
   res = requests.post(url=url,data=data,headers=headers)

   print(res.status_code)
   print(res.text)


 
def owner_todos():

   url = 'http://localhost:8000/todos/owner_todos'
   
   headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODAwMDg4LCJpYXQiOjE3MzE3OTY0ODgsImp0aSI6ImMxMDE2YmYwODczNDQ2YTU5NjBiZmM0MmM2NGVjNzQwIiwidXNlcm5hbWUiOiJtYXJpYW4xMjM0NTYifQ.B4DB5eil8B03j8k6OcjNKYoi2nt03ewr5cIj43zp8pY'
            }

   res = requests.get(url=url,headers=headers)

   print(res.status_code)
   print(res.text)



 
def update_todo():
# puntem task_id care apartine altui user si token altui user
# task_id belongs to marianmarian
   url = 'http://localhost:8000/todos/update_todo?task_id=8f3d52b5-f3db-45f4-a89a-bfe0f1710340'

# task_id not belong to mairan123456 
#    url = 'http://localhost:8000/todos/update_todo?task_id=81d3c1a6-d717-4f02-b0c5-8ea7e839762f'

   
   headers = {
#    token for marian123456
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODA3NDI1LCJpYXQiOjE3MzE4MDM4MjUsImp0aSI6ImQ4N2VkZjMyMzEzYTQwMGNhNzkxOGJmODI3NGU2Mjg2IiwidXNlcm5hbWUiOiJtYXJpYW4xMjM0NTYifQ.4QRL1MgKZ5aRIStA5qVmq4PNeNe9mM3ZusHx-aSUhTI'
            }
   data = {'task':'chaneged ``j  ','completed':True}
#    data = {}
   res = requests.put(url=url,data=data,headers=headers)

   print(res.status_code)
   print(res.text)



def update_todo_complete_field():
# puntem task_id care apartine altui user si token altui user
# task_id belongs to marianmarian
   url = 'http://localhost:8000/todos/update_complete_field/8f3d52b5-f3db-45f4-a89a-bfe0f1710340'

# task_id not belong to mairan123456 
#    url = 'http://localhost:8000/todos/update_complete_field/81d3c1a6-d717-4f02-b0c5-8ea7e839762f'

   
   headers = {
#    token for marian123456
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODY1Njk4LCJpYXQiOjE3MzE4NjIwOTgsImp0aSI6IjhhNGQ0MDY0ZTY5MTQ2Y2FiYTk5MDlhZTI5ODUzY2MwIiwidXNlcm5hbWUiOiJtYXJpYW4xMjM0NTYifQ.soRoY2ZrNJ0uFxFmv1CAoMbzNGX3GFaoKpJh1WaVgAQ'
            }
   data = {'completed': 'awd'}
#    data = {}
   res = requests.patch(url=url,data=data,headers=headers)

   print(res.status_code)
   print(res.text)




def remove_todo():
# puntem task_id care apartine altui user si token altui user
# task_id belongs to marianmarian
   url = 'http://localhost:8000/todos/remove_todo/8f3d52b5-f3db-45f4-a89a-bfe0f1710340'

# task_id not belong to mairan123456 
#    url = 'http://localhost:8000/todos/update_complete_field/81d3c1a6-d717-4f02-b0c5-8ea7e839762f'

   
   headers = {
#    token for marian123456
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxODY1Njk4LCJpYXQiOjE3MzE4NjIwOTgsImp0aSI6IjhhNGQ0MDY0ZTY5MTQ2Y2FiYTk5MDlhZTI5ODUzY2MwIiwidXNlcm5hbWUiOiJtYXJpYW4xMjM0NTYifQ.soRoY2ZrNJ0uFxFmv1CAoMbzNGX3GFaoKpJh1WaVgAQ'
}
   res = requests.delete(url=url,headers=headers)

   print(res.status_code)
   print(res.text)






if __name__ == '__main__':

    if sys.argv[1] == 'all_todos':
        get_all_todos()
    elif sys.argv[1] == 'create_todo':
        create_todo()
    elif sys.argv[1] == 'owner_todos':
        owner_todos()
    elif sys.argv[1] == 'update_todo':
        update_todo()
    elif sys.argv[1] == 'update_todo_complete_field':
        update_todo_complete_field()
    elif sys.argv[1] == 'remove_todo':
        remove_todo()

 
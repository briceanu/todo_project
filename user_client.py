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
def create_user():

    url = 'http://localhost:8000/users/create'

    data = {
            'username':'marian1234',
            'password':'awdawd283AWDawdadwd',
            'confirm_password':'awdawd283AWDawdadwd',
            'email':'marian@gmail.com'
            }

    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.text)



def list_users():

    url = 'http://localhost:8000/users/list'

    res = requests.get(url=url)

    print(res.status_code)
    print(res.text)




def signIn():

    url = 'http://localhost:8000/users/signin'

    data = {
            # 'username':'gigi1232d',
            'username':'marian1234',
            'password':'awdawd283AWDawdadwd',
            }

    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.text)




def new_access_token():

    url = 'http://localhost:8000/users/new_access_token'

    headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTYxNzEwMSwiaWF0IjoxNzMxNTMwNzAxLCJqdGkiOiI0M2E2ZmFmMmU3ZGY0ZGRjYWNjODFiNGQwYzFhZjJmYSIsInVzZXJuYW1lIjoiZ2lnaTEyMzJkIn0.f-97ytxKM6czZGUwg-BC1vX0ugP35Ui7nr8blKzU3KY'
            }

    # headers = {
    #     'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTYxNzEwMSwiaWF0IjoxNzMxNTMwNzAxLCJqdGkiOiI0M2E2ZmFmMmU3ZGY0ZGRjYWNjODFiNGQwYzFhZjJmYSIsInVzZXJuYW1lIjoiZ2lnaTEyMzJhd2RkIn0.qgxorAdPFf1avDFcTiT1CWBQeiToVlIQh4zpHTtnsk0'
    #         }

    res = requests.post(url=url,headers=headers)

    print(res.status_code)
    print(res.text)



def logout():

    url = 'http://localhost:8000/users/logout'

    data = {
        'refresh_token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNTQxMzYwLCJpYXQiOjE3MzE1Mzc3NjAsImp0aSI6IjdmNzAyNGIzMjFlYzRiODA4MTUwYjJkMTk2YjRhNjYxIiwidXNlcm5hbWUiOiJnaWdpMTIzMmQifQ.T2g4FGtlmxP4Bac4jmexVz5Reytb45gDplxlyiqlI04'
            }



    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.text)


def remove_user():

   url = 'http://localhost:8000/users/remove_user'
   
   headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNTQzNjIyLCJpYXQiOjE3MzE1NDAwMjIsImp0aSI6IjIyNWE5Yzc1YzEyMTRiMWFhZWZiYzRlOTJjYWVlMjA1IiwidXNlcm5hbWUiOiJnaWdpIn0.Ipy7PF3oKxFd3VyhCgB-RO4Dm_FZG0dqV9LhSsOXjqo'
            }
   data = {'username':'awdawd'}
#    data = {}
   res = requests.delete(url=url,data=data,headers=headers)

   print(res.status_code)
   print(res.text)


def update_user():

    url = 'http://localhost:8000/users/update_user'


    headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNTk1MjkxLCJpYXQiOjE3MzE1OTE2OTEsImp0aSI6IjAzNDcyODg4ZDJiODQ3OTZhMWFhZWFhZjRkZjg1MWJmIiwidXNlcm5hbWUiOiJtYXJpYW4xMjMifQ.yn745E7gYRLT6HQ6WtiJ_3xDggdo2UAbHYOmwkoOLG4'
            }

    data = {
            'username':'marian8888',
            'password':'awdawd283AWDawdsef',
            'confirm_password':'awdawd283AWDawdsef',
            'email':'marian888@gmaawdawwdil.com'
            }

    res = requests.put(url=url,data=data, headers=headers)

    print(res.status_code)
    print(res.text)



def update_user_password():

    url = 'http://localhost:8000/users/update_password'


    headers = {
        'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNjA4MzEwLCJpYXQiOjE3MzE2MDQ3MTAsImp0aSI6ImYwOTQ0MzFmM2U0ZTQzMjA4YjNjYjc1YmNkYWM1ZThhIiwidXNlcm5hbWUiOiJtYXJpYW4xMjM0In0.Y8l1ufpYbOcdRcqq-I9fnqBvnrIte83fanSka--oQLE'
            }
# old marian1234    new ===> marian12345
#  old awdawd283AWDawdadwd    new ==> awidm23JJJ
    data = {
            'username':'marian12345',
            'password':'aw2L',
            'confirm_password':'aw2L',
            'email':'marian1234@gmaawdawwdilggigi.com'
            }

    res = requests.patch(url=url,data=data, headers=headers)

    print(res.status_code)
    print(res.text)








if __name__ == '__main__':

    if sys.argv[1] == 'create_user':
        create_user()
    elif sys.argv[1] == 'list_users':
        list_users()
    elif sys.argv[1] == 'sign_in':
        signIn()
    elif sys.argv[1] == 'new_access_token':
        new_access_token()
    elif sys.argv[1] == 'logout':
        logout()
    elif sys.argv[1] == 'remove_user':
        remove_user()
    elif sys.argv[1] == 'update_user':
        update_user()
    elif sys.argv[1] == 'update_user_password':
        update_user_password()
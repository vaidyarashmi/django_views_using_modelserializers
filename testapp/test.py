import requests
import json
BASE_URL='http://127.0.0.1:8000/'
END_URL='api/'

# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+END_URL,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource()

# def create_resource():
#     new_emp={
#         'eno':4000,
#         'ename':'pooja',
#         'esal':300,
#         'eaddr':'Pune'
#     }
#     resp=requests.post(BASE_URL+END_URL,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()
def update_resource(id):
    new_emp={
        'id':id,
        'ename':'puja',
        'esal':9000000,
    }
    resp=requests.put(BASE_URL+END_URL,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
update_resource(4)

# def delete_resource(id):
#     data={
#         'id':id,
#     }
#     resp=requests.delete(BASE_URL+END_URL,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(6)
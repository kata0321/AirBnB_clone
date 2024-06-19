#!/usr/bin/python3
from models.base_model import BaseModel

bm1 = BaseModel()
bm1.name = "My_First_Model"
bm1.my_number = 89
print(bm1.id)
print(bm1)
print(type(bm1.created_at))
print("--")
bm1_json = bm1.to_dict()
print(bm1_json)
print("JSON of bm1:")
for key in bm1_json.keys():
    print("\t{}: ({}) - {}".format(key, type(bm1_json[key]), bm1_json[key]))

print("--")
bm2 = BaseModel(**bm1_json)
print(bm2.id)
print(bm2)
print(type(bm2.created_at))

print("--")
print(bm1 is bm2)

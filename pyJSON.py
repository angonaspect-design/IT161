#
import json


#
data1 = {

    'name': 'Ryu Endo',
    'age':22,
    'city':'Seattle, WA',
    'interests':['Sports','Video Game','Music'],
    'is_student': True

}

with open('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4)

print("Data has been written to data1.json")




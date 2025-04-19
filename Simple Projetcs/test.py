import json

test_data = {"name": "item",
             "quantity": 10}
with open("test.json","w")as file:
    json.dump(test_data,file)
    print("Test file created Successfully")
person = {
    "name" : "ramesh",
    "age" : 24,
    "hobby" : ["football","fifa"],
    "family":[
        {
            "relation":"mother",
            "name" : "sita"   
        },
        {
            "relation":"father",
            "name" : "rajesh"   
        },
        {
            "relation":"sister",
            "name" : "sabita"   
        }
    ]
}

print("name :", person['name'])
print("hobby :" ,person["hobby"][0])
for i in person["family"]:
    if i["relation"] == 'mother':
        mother_name = i['name']
print("Mother :", mother_name)
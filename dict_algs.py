#Workers with kids older 18 years func:
def findWorkers(allWorkers, age_of_child):
    filtered = []
    for worker in allWorkers:
        for i in range(len(worker['children'])):
            if worker['children'][i]['age'] > age_of_child:
                filtered.append(worker['name'])
    return filtered


ivan = {
    "name": "Ivan",
    "age": 31,
    "children": [{
        "name": "Vasja",
        "age": 12,
    }, {
        "name": "Petja",
        "age": 10,
    }]
}
darja = {
    "name": "Darja",
    "age": 41,
    "children": [{
        "name": "Kirill",
        "age": 21,
    }, {
        "name": "Pavel",
        "age": 15,
    }]
}

emps = [ivan, darja]

findWorkers(emps, 18)

print("Workers, who entered the filtration: ")
print( findWorkers(emps, 18) )

input()


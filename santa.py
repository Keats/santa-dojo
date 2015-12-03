import json

with open("tiger/tiger.json") as f:
    data = f.read()
    gifts = json.loads(data)

    actual_gifts = []
    for gift in gifts:
        if gift["price"] is None or gift["pic"] is None or gift["name"] is None:
            continue
        actual_gifts.append(gift)

    for g in actual_gifts:
        print("%s - %s - %s" %(g["name"], g["pic"], g["price"]))

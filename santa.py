import json

with open("tiger/tiger.json") as f:
    data = f.read()
    gifts = json.loads(data)

    actual_gifts = []
    for gift in gifts:
        if gift["price"] is None or gift["pic"] is None or gift["name"] is None:
            continue
        actual_gifts.append(gift)

    with open("cleaned_tigers.json", "w") as f:
        f.write(json.dumps(actual_gifts))


import random

ducks_and_weight = {
    "partyduck": 1000,
    "partyduck_dance1": 1000,
    "partyduck_dance2": 1000,
    "partyduccc": 200,
    "party-dinosaur": 1,
}

num_ducks = 100

ducks = [f":{d}:" for d in random.choices(list(ducks_and_weight.keys()), list(ducks_and_weight.values()), k=num_ducks)]

slack_string = ''.join(ducks)
print(f"{slack_string}")

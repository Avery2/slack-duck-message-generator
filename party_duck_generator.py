import random

ducks_and_weight = {
    "partyduck": 1000,
    "partyduck_dance1": 1000,
    "partyduck_dance2": 1000,
    "partyduccc": 200,
    "party-dinosaur": 1,
    "space": 1000,
    "newline": 50
}

num_ducks = 100

def slack_token(duck):
    if duck == "space":
        return " "
    if duck == "newline":
        return "\n"
    return f":{duck}:"

ducks = [slack_token(d) for d in random.choices(list(ducks_and_weight.keys()), list(ducks_and_weight.values()), k=num_ducks)]

slack_string = ''.join(ducks)
print(f"{slack_string}")

import random

ducks_and_weight = {
    "partyduck": 100,
    "partyduck_dance1": 100,
    "partyduck_dance2": 100,
    "partyduccc": 20,
    "party-dinosaur": 1,
    "space": 100,
    "newline": 5
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

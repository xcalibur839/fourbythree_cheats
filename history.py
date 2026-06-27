import json, datetime as dt

def generate(games: list, genesis_date: dt.datetime = dt.datetime.strptime("2026-06-11", "%Y-%m-%d")):
    source = {}
    with open("history.json", "r") as hist:
        source = json.load(hist)
    
    for game in games:
        for key, vals in game.items():
            if key not in source:
                source[key] = {
                    "s": 206 + (dt.date.fromisoformat(key) - genesis_date.date()).days,
                    "m": 0,
                    "w": 1,
                    "hf": 1,
                    "hm": 0,
                    "pf": 1,
                    "bf": 0,
                    "rr": 1,
                    "rw": 0,
                    "gr": 0,
                    "gu": 0,
                    "gd": 0,
                    "db": 1,
                    "fast": 1,
                    "rb": 0,
                    "p": 1,
                    "ad": 1,
                    "gold": 1,
                    "silver": 0,
                    "rel": 1,
                }

            source[key]['ms'] = vals['sms']
            source[key]['ts'] = vals['t0']

    return source

if __name__ == "__main__":
    game = [{
        "2026-06-26": {
            "v":1,
            "s":"CATCH",
            "slots0":[
                "CATCH",
                "BOUNTY",
                "YIELD",
                "LATCH",
                "BOLT",
                "GEM",
                "KEEPER",
                "NAB",
                "GRAB"
            ],
            "solved":[3,0,1,2],
            "m":0,
            "p":0,
            "g":[
                ["CATCH","BOUNTY","YIELD"],
                ["CATCH","LATCH","BOLT"],
                ["CATCH","GEM","KEEPER"],
                ["CATCH","NAB","GRAB"]
            ],
            "over":True,
            "t0":1782489347763,
            "sms":44768,
            "ad":1
        }
    }]

    print(generate(game))
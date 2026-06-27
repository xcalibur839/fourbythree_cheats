import json, base64, random, time

puzzles = None
with open("www.hankgreen.com/fourbythree/puzzles.json", "r") as puzz_file:
    puzzles = json.load(puzz_file)

def solve(key: str, t0: int = 0, sms: int = 0) -> dict:
    result = {}

    fmt_puzz = str(puzzles[key]).replace("-", "+").replace("_", "/")
    while(len(fmt_puzz) % 4):
        fmt_puzz += "="
    puzz_data = json.loads(base64.b64decode(fmt_puzz).decode())
    special = puzz_data['s']
    categories = puzz_data['c']

    if t0 != 0:
        timestamp = t0
    else:
        year, month, day = key.split("-")
        timestamp = int(time.mktime((
            int(year),              #tm_year
            int(month),             #tm_mon
            int(day),               #tm_mday
            0,                      #tm_hour
            random.randint(7, 47),  #tm_min
            random.randint(0, 59),  #tm_sec
            0,                      #tm_wday
            0,                      #tm_yday
            -1                      #tm_isdst
        )) * 1000)

    entry = {
        "v": 1,
        "s": special,
        "slots0": [
            special,
            categories[3][1],
            categories[3][2],
            categories[0][1],
            categories[0][2],
            categories[1][1],
            categories[1][2],
            categories[2][1],
            categories[2][2]
        ],
        "solved": [3, 0, 1, 2],
        "m": 0,
        "p": 0,
        "g": [
            [
                special,
                categories[3][1],
                categories[3][2]
            ],
            [
                special,
                categories[0][1],
                categories[0][2]
            ],
            [
                special,
                categories[1][1],
                categories[1][2]
            ],
            [
                special,
                categories[2][1],
                categories[2][2]
            ]
        ],
        "over": True,
        "t0": timestamp,
        "sms": 30000 + random.randint(5000, 15000) if sms == 0 else sms,
        "ad": 1
    }

    result[key] = entry

    return result

if __name__ == "__main__":
    results = []
    start_num = 26
    end_num = 11
    current_num = start_num

    while(current_num >= end_num):
        key = f"2026-06-{current_num}"
        results.append(solve(key))
        current_num -= 1

    print("Game Data")
    for result in results:
        for game, vals in result.items():
            entry = f"localStorage.setItem('x43_game_{game}','{json.dumps(vals).replace(" ", "")}')"
            print(entry, end="\n\n")
            input()

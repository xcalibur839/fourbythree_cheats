#built-ins
import argparse, json
from datetime import datetime, timedelta
#pip installed
import pyperclip
#custom modules
import puzzle, history

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--limit", type = int, default = 0)
parser.add_argument("-d", "--date", help = "Must be in the format YYYY-MM-DD")
parser.add_argument("-t", "--time", type = int, default = 0, help = "Time it took to solve the puzzle in milliseconds. Will be applied to all puzzles")
parser.add_argument("-s", "--solved", type = int, default = 0, help = "Unix Epoch timestamp of when the puzzle was solved in milliseconds. Will be applied to all puzzles")
args = parser.parse_args()

results = []
genesis_date = datetime.strptime("2026-06-11", "%Y-%m-%d")
working_date = datetime.now() if args.date is None else datetime.strptime(args.date, "%Y-%m-%d")
solved_count = 0

hist_data = {}
with open("history.json", "r") as hist_file:
    hist_data = json.load(hist_file)

while(working_date >= genesis_date):
    formatted_date = working_date.strftime("%Y-%m-%d")
    working_date -= timedelta(days = 1)
    if formatted_date in hist_data:
        continue

    results.append(puzzle.solve(formatted_date, t0 = args.time, sms = args.solved))
    solved_count += 1
    if args.limit != 0 and solved_count >= args.limit:
        break

if not len(results) > 0:
    print("No new game data was generated because you already have the top score")
    quit()

game_entry = ""
print("Game Data")
for game, vals in results[0].items():
    game_entry += f"localStorage.setItem('x43_game_{game}','{json.dumps(vals).replace(" ", "")}'); "
print(game_entry, end = "\n\n")

hist = history.generate(results)
hist_entry = f"localStorage.setItem('x43_history', '{json.dumps(hist)}'); "
print("History")
print(hist_entry, end = "\n\n")

hist_len = len(hist)
best = 205 + hist_len
stats_entry = f"localStorage.setItem('x43_stats', '{json.dumps({
    "played": hist_len,
    "won": hist_len,
    "perfect": hist_len,
    "best": best,
    "points": int((hist_len / 2) * (206 + best))
})}'); "
print("Stats")
print(stats_entry)

pyperclip.copy(game_entry + hist_entry + stats_entry + "restoreGame(loadGame()); endGame(); location.reload();")
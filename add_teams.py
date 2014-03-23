import random
from core import *

def teams():
    return set(json.load(open("teams.json")).keys()) - set(["SRZ"])

if __name__ == "__main__":
    random.seed("student robotics seed lol")

    shuffled_teams = list(teams())
    random.shuffle(shuffled_teams)

    schedule = open(schedule_file_name(len(teams())-1)).read()
    lines = schedule.split("\n")
    build = ""
    for line in lines:
        if len(line) == 0:
            continue

        if line.strip()[0] == "#":
            build += line
        else:
            parts = line.split("|")
            parts = [shuffled_teams[int(part)] if part != "x" else part for part in parts]
            build += "|".join(parts)
        build += "\n"

    with open("54_with_names.txt", "w") as fp:
        fp.write(build)

import json
import os

def teams_per_match():
    return 4

def missing_team_character():
    return "x"

def schedule_file_name(match_number):
    return "processed_schedules/%03d.txt" % (match_number + 1)

def seed_schedule_lengths():
    return [int(x.split(".")[0]) for x in os.listdir("seed_schedules")]

def teams():
    return set(json.load(open("teams.json")).keys()) - set(["SRZ"])

def next_multiple_of_4_above(i):
    return (i + 3) & ~0x03

def seed_file_name(i):
    return "seed_schedules/" + str(next_multiple_of_4_above(i)) + ".txt"

def replace_teams_below(i, string):
    lines = string.split("\n")
    build = ""
    for line in lines:
        if len(line) == 0:
            continue

        if line.strip()[0] == "#":
            build += line
        else:
            parts = line.split("|")
            parts = [missing_team_character() if int(part) > i else part for part in parts]
            build += "|".join(parts)
        build += "\n"

    return build

if __name__ == "__main__":
    max_team_count = len(teams())

    min_team_count = min(seed_schedule_lengths()) - teams_per_match() + 1
    print max_team_count
    print min_team_count

    for i in xrange(min_team_count, max_team_count):
        with open(schedule_file_name(i), "w") as fp:
            fp.write(replace_teams_below(i, open(seed_file_name(i)).read()))

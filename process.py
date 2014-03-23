from core import *

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

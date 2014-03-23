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


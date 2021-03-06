#!/usr/bin/env python

"""
Helper script to restore the round number comments in a schedule if they
are removed by automated tooling. Does not cope with being run on a
schedule which already has round numbers in it.
"""

from __future__ import print_function

import math

NUM_TEAMS = 48
FILE = 'seed_schedules/{0}.txt'.format(NUM_TEAMS)

TEAMS_PER_ROUND = int(math.ceil(NUM_TEAMS / 8.0))

with open(FILE, 'r') as f:
    lines = f.readlines()

for i in reversed(range(0, len(lines), TEAMS_PER_ROUND)):
    round_num = int(math.ceil(i / 8.0))
    lines.insert(i, "# r{0}\n".format(round_num))

with open(FILE, 'w') as f:
    f.write(''.join(lines))

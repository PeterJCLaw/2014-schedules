# SRobo match schedules

This repo contains schedules which were generated in 2014 by the SAT solver
implemented in https://github.com/jmorse/numbness. See the discussion at
http://thread.gmane.org/gmane.science.robotics.srobo.devel/718 for more
details.

Those schedules have been further modified by various tooling (and by hand)
to ensure that they meet the criteria desired for SR match schedules.

Schedule testing is typically done using the scripts found at:
https://www.studentrobotics.org/cgit/comp/match-scheduler2.git/tree/checks

The `restore-round-comments.py` script exists to restore round-number comments
when the output of those scripts removes them.

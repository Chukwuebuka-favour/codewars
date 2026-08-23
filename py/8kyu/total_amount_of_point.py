'''

Description:
Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4

'''

# MY SOLUTION
def points(games):
    points = 0
    for game in games:
        our_team_score = game.split(':')[0]
        opponent_score = game.split(':')[-1]

        if our_team_score > opponent_score:
            points += 3
        elif our_team_score == opponent_score:
            points += 1
        else:
            points += 0
    return points


# ALTERNATIVE SOLUTION
def points(games):
    return sum(3 if x > y else 0 if x < y else 1 for x, y in (score.split(":") for score in games))
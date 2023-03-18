#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    unique_ranks = list(sorted(set(ranked), reverse=True))
    player_ranks = []

    idx = len(unique_ranks) - 1  # Start from the last rank

    for score in player:
        # Compare player's score with the ranked leaderboard
        # and find the appropriate rank by iterating from the lowest rank
        while idx >= 0 and score >= unique_ranks[idx]:
            idx -= 1
        
        # Calculate player's rank based on the found index
        if idx == -1:
            player_rank = 1
        else:
            player_rank = idx + 2

        player_ranks.append(player_rank)

    return player_ranks
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

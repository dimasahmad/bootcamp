# climbing the leaderboard
# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbing_leaderboard(ranked_scores: list[int], player_scores: list[int]) -> list[int]:
    """Determine each player's rank after each new score with dense ranking method

    Args:
        ranked (list[int]): the leaderboard scores
        player (list[int]): the player's scores

    Returns:
        list[int]: the player's rank after each new score
    """

    # remove duplicate scores
    ranked_scores = sorted(set(ranked_scores), reverse=True)

    # ranks of the player's scores
    ranks: list[int] = []

    rank: int = len(ranked_scores)

    for player_score in player_scores:
        # iterate rank upwards
        while rank > 0 and player_score >= ranked_scores[rank - 1]:
            rank -= 1
        ranks.append(rank + 1)

    return ranks

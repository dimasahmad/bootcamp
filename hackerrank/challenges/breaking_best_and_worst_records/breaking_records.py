# breaking the records
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breaking_records(scores: list[int]) -> list[int]:
    """Count how many times Maria broke her best and worst records

    Args:
        scores (list[int]): score of each games

    Returns:
        list[int]: count of how many times she broke her records
        first element ([0]) is best count, and second element ([1]) is worst count
    """

    best_score: int = None
    worst_score: int = None

    breaking_best: int = 0
    breaking_worst: int = 0

    for score in scores:
        # initialize best and worst with first score
        if best_score == worst_score == None:
            best_score = worst_score = score
            continue

        if score > best_score:
            best_score = score
            breaking_best += 1

        if score < worst_score:
            worst_score = score
            breaking_worst += 1

    return [breaking_best, breaking_worst]

# apple and orange
# https://www.hackerrank.com/challenges/apple-and-orange/problem

def count_apples_and_oranges(house_position_start: int, house_poisition_end: int, apple_tree_position: int, orange_tree_position: int, apples_distance_from_tree: list[int], oranges_distance_from_tree: list[int]) -> None:
    """Count the number of apples and oranges that land on a house"""

    apples_position: list[int] = [apple_tree_position + distance
                                  for distance in apples_distance_from_tree]
    oranges_position: list[int] = [orange_tree_position + distance
                                   for distance in oranges_distance_from_tree]

    apples_landed_on_house: list[int] = [position
                                  for position in apples_position
                                  if position >= house_position_start and position <= house_poisition_end]
    oranges_landed_on_house: list[int] = [position
                                   for position in oranges_position
                                   if position >= house_position_start and position <= house_poisition_end]

    print(len(apples_landed_on_house))
    print(len(oranges_landed_on_house))

# electronics shop
# https://www.hackerrank.com/challenges/electronics-shop/problem

def get_money_spent(keyboards: list[int], drives: list[int], budget: int) -> int:
    """Find the cost to buy the most expensive computer keyboard and USB drive that can be purchased with a given budget

    Args:
        keyboards (list[int]): keyboard prices
        drives (list[int]): drive prices
        budget (int): budget

    Returns:
        int: the maximum that can be spent, or `-1` if it is not possible to buy both items
    """

    max_price: int = -1

    for i in range(len(keyboards)):
        for j in range(len(drives)):
            price: int = keyboards[i] + drives[j]
            if price <= budget and price > max_price:
                max_price = price

    return max_price

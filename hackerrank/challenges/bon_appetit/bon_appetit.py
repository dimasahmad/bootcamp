# bill division
# https://www.hackerrank.com/challenges/bon-appetit/problem

def bon_appetit(bill: list[int], k: int, bill_charged: int) -> None:
    """Determine if Brian didn't overcharge Anna for the split bill.

    Print "Bon Appetite" if the amount is right.
    Otherwise, print the amount of money Brian owes to Anna.

    Args:
        bill (list[int]): list of bill
        k (int): index of item Anna didn't eat
        bill_charged (int): price charged by Brian
    """

    # Remove item that Anna didn't eat
    bill.pop(k)
    bill_actual: int = sum(bill)

    if bill_actual / 2 == bill_charged:
        print("Bon Appetit")
    else:
        # overcharged, calculate the difference
        print(bill_charged - int(bill_actual / 2))

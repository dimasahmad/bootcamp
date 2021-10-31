# angry professor
# https://www.hackerrank.com/challenges/angry-professor/problem

def angry_professor(k: int, a: list[int]) -> str:
    """Determine if class is cancelled
    
    Given the arrival time of each student and a threshhold number of attendees,
    determine if the class is cancelled.
    
    Args:
        k (int): threshold number of students
        a (list[int]): arrival times of the `n` students, `<= 0` means on time, `> 0` means late

    Returns:
        string: `YES` if class is cancelled, or `NO` if class is not cancelled
    """
    
    return "YES" if sorted(a)[k-1] > 0 else "NO"

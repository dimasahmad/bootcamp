# stuttering
# https://edabit.com/challenge/gt9LLufDCMHKMioh2


def stutters(txt: str) -> str:
    return f'{txt[:2]}... {txt[:2]}... {txt}?'
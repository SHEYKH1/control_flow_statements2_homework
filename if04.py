def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
        return 0
    elif a>b:
        return a
    else:
        return b
a=7
b=5
ans=main(a,b)
print(ans)    
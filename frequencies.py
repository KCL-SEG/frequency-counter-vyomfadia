"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    # Use list comprehension to convert all values to a string.
    # Could also be done using map
    items = [str(x) for x in items]
    for item in items:
        frequencies[item] = frequencies.get(item, 0) + 1

    return frequencies

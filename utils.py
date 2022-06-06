"""
Some utils for other scripts. Actually, just one for now, a function
to transfer either number of lists of numbers into strings of the
desired form.
"""

def textify_numbers(nums):
    if hasattr(nums, '__iter__'):
        input = ', '.join(map(str, nums))
    else:
        input = str(nums)
    return input

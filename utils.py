def textify_numbers(nums):
    if hasattr(nums, '__iter__'):
        input = ', '.join(map(str, nums))
    else:
        input = str(nums)
    return input
# def add_two(nums):
#     for i in nums:
#         for j, value in enumerate(i):
#             i[j] += 2
#
#     return nums

def add_two(nums):
    return [[num + 2 for num in i] for i in nums]




print(add_two([[1, 2, 3] , [4, 5, 6]]))

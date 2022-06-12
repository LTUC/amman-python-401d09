from collections import Counter

nums = Counter([1,2,3,1])
nums = Counter({1:2, 2:1, 3:1})
pets = Counter(cats = 4, dogs = 4, lion = 1)
print(nums)
print(pets)

nums = Counter([1,2,3,1,2,2])

print(nums.most_common())
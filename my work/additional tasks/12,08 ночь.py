# уебанство
# def missing_no(nums):
#     sum_0 = (100 * 101) // 2
#     sum_1 = sum(nums)
#     miss_num = sum_0 - sum_1
#     return miss_num


# божество
# def missing_no(nums):
#     sum_0 = len(nums) * (len(nums) + 1) // 2
#     sum_1 = sum(nums)
#     miss_num = sum_0 - sum_1
#     return miss_num


# def friends(x):
#     friend = []
#
#     for name in x:
#         if len(name) == 4:
#             friend.append(name)
#         else:
#             continue
#
#     return friend
#
#
# input1 = ["Ryan", "Kieran", "Jason", "Yous"]
# print(friends(input1))

# def get_min_max(seq):
#     min_val = seq[0]
#     max_val = seq[0]
#
#     for i in seq:
#         if i < min_val:
#             min_val = i
#         if i > max_val:
#             max_val = i

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# even_numbers = []
# odd_numbers = []
#
# for i in numbers:
#     if i % 2 == 0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
#
# print(f"even numbers: {even_numbers}, odd numbers: {odd_numbers}")


# 1000-7
# ghole = 1000
# count = 1
# while ghole >= 0:
#     print(ghole, end=" ")
#     count += 1
#     if count % 18 == 0:
#         print()
#     ghole -= 7

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_numbers = 0
# product_numbers = 1
#
# for i in numbers:
#     sum_numbers += i
#     product_numbers *= i
#
# print(f"Sum of numbers: {(sum_numbers)}, Product of squares: {product_numbers}")

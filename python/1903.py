# def largestOddNumber(num: str) -> str:  # parsing every char
#     for i in range(len(num) - 1, -1, -1):
#         if int(num[i]) % 2 == 1:
#             return num[:i + 1]
#     return ""


# def largestOddNumber(num: str) -> str:
#     for i in range(len(num) - 1, -1, -1):
#         if num[i] in ["1", "3", "5", "7", "9"]:
#             return num[0: i + 1]
#     return ""




# Arrays: Left Rotation

# A left rotation operation on an array of size  shifts each of the array's elements  unit to the left.
# For example, if left rotations are performed on array , then the array would become.

# Given an array of  integers and a number, , perform  left rotations on the array.
# Then print the updated array as a single line of space-separated integers.

# Sample Input
#
# 5 4
# 1 2 3 4 5
#
# Sample Output
#
# 5 1 2 3 4

# n = integers
# k = left-rotations
# a = array


def array_left_rotation(a, n, k):
    for count in range(0, k):
        temp = a[0]
        for index in range(0, n - 1):
            print("ran")
            a[index] = a[index + 1]
        a[len(a) - 1] = temp

    return a


# Recursive Approach
# def array_left_rotation(a, n, k):
#     if k > 0:
#         shifted_array = []
#         original_first = a[0]
#         for index in range(1, n):
#             shifted_array.append(a[index])
#         shifted_array.append(original_first)
#         return array_left_rotation(shifted_array, n, k - 1)
#     else:
#         return a


def main():
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, k);
    print(*answer, sep=' ')


main()

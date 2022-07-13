import random


def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr) / 2)
        lhs = arr[:mid]
        rhs = arr[mid:]
        merge_sort(lhs)
        merge_sort(rhs)

        i = j = 0
        for k in range(0, len(arr)):
            if (j >= len(rhs)) or (i < len(lhs) and lhs[i] <= rhs[j]):
                arr[k] = lhs[i]
                i += 1
            else:
                arr[k] = rhs[j]
                j += 1


if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(1000)]
    print('Before')
    print(arr)
    merge_sort(arr)
    print('After')
    print(arr)

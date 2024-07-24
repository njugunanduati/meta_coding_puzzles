from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    result =  0
    S.sort()
    left = 1
    for s in S:
        right = s - (K + 1)
        result += 1 + (right - left) // (K + 1)
        left = s + (K + 1)
    result += 1 + (N - left) // (K + 1)
    return result


if __name__ == '__main__':
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    print(getMaxAdditionalDinersCount(N, K, M, S))  # Output: 2
    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]
    # print(getMaxAdditionalDinersCount(N, K, M, S))  # Output: 2
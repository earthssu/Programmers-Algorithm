import collections


def dfs(nums, i, n, t):
    ret = 0
    if i == len(nums):
        if n == t:
            return 1
        else:
            return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret


def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer


def solution_bfs(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))

    return answer
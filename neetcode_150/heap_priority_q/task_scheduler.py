import heapq
from collections import Counter, deque
from typing import List



# My brute-force
# def leastInterval(tasks: List[str], n: int) -> int:
#     if n == 0:
#         return len(tasks)
#
#     tasks_map = {}
#     for task in tasks:
#         if task in tasks_map:
#             tasks_map[task]['count'] += 1
#         else:
#             tasks_map[task] = {
#                 'count': 1,
#                 'available': True,
#                 'left_cd': 0
#             }
#
#     arr = []
#     i = len(tasks)
#     while i > 0:
#         task = get_most_freq(tasks_map)
#         arr.append(task)
#         if task != 'idle':
#             tasks_map[task]['count'] -= 1
#             tasks_map[task]['available'] = False
#             tasks_map[task]['left_cd'] = n
#             i -= 1
#         process_cds(task, tasks_map)
#
#     return len(arr)
# def get_most_freq(tasks_map):
#     freq = 'idle'
#     cur_max_count = 0
#     for task in tasks_map:
#         if tasks_map[task]['available'] and tasks_map[task]['count'] > cur_max_count:
#             cur_max_count = tasks_map[task]['count']
#             freq = task
#     return freq
# def process_cds(cur_task, tasks_map):
#     for task in tasks_map:
#         if task == cur_task:
#             continue
#         if tasks_map[task]['left_cd'] > 0:
#             tasks_map[task]['left_cd'] -= 1
#         tasks_map[task]['available'] = tasks_map[task]['left_cd'] == 0


# T: O(n*m), m = idle time
# M: O(n)
def leastInterval(tasks: List[str], n: int) -> int:
    count = Counter(tasks)
    max_heap = [-c for c in count.values()]
    heapq.heapify(max_heap)
    q = deque()  # [-c, time_at_which_c_is_available_again]
    time = 0

    while max_heap or q:
        time += 1

        if max_heap:
            c = 1 + heapq.heappop(max_heap)
            if c:
                q.append([c, time+n])

        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])

    return time

"""
A: 3
B: 3
"""
"""
A: 6
B: 1
C: 1
D: 1
E: 1
F: 1
G: 1
"""


if __name__ == '__main__':
    tasks1, n1 = ["A","A","A","B","B","B"], 2
    tasks2, n2 = ["A","A","A","A","A","A","B","C","D","E","F","G"], 2
    tasks3, n3 = ["A", "A", "A", "B", "B", "B"], 0

    ans1 = leastInterval(tasks1, n1)
    ans2 = leastInterval(tasks2, n2)
    ans3 = leastInterval(tasks3, n3)

    print(ans1)
    print(ans2)
    print(ans3)

    assert ans1 == 8
    assert ans2 == 16
    assert ans3 == 6

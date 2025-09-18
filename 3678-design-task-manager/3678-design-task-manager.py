import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}  # taskId -> (userId, priority)
        self.heap = []   # max-heap simulation using (-priority, -taskId, userId)
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.tasks:
            userId, _ = self.tasks[taskId]
            self.tasks[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.tasks:
            del self.tasks[taskId]
        # we don't touch the heap → lazy deletion will handle it

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, userId = heapq.heappop(self.heap)
            taskId = -negTaskId
            if taskId in self.tasks:
                uId, pr = self.tasks[taskId]
                if pr == -priority and uId == userId:
                    del self.tasks[taskId]
                    return userId
        return -1

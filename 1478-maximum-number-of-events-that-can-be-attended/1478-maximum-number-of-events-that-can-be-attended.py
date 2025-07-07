class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        event_pointer = 0
        min_heap = []
        max_day = max(end for _, end in events)
        attended = 0

        for day in range(1, max_day + 1):
            while event_pointer < len(events) and events[event_pointer][0] == day:
                heapq.heappush(min_heap, events[event_pointer][1])
                event_pointer +=1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
        return attended
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = list(range(k))
        heapq.heapify(available)

        busy = []

        count = [0] * k

        for i ,(start, duration) in enumerate(zip(arrival,load)):
            while busy and busy[0][0] <= start:
                _, server_id = heapq.heappop(busy)

                next_val = i + (server_id - i) % k
                heapq.heappush(available, next_val)

            if not available:
                continue
            
            assigned_server = heapq.heappop(available) % k
            count[assigned_server] += 1

            heapq.heappush(busy, (start + duration, assigned_server))

        max_request = max(count)
        return [server_id for server_id, c in enumerate(count) if c == max_request]

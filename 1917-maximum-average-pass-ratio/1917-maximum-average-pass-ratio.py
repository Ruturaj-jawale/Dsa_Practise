class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """

        def gain(p,t):
            return (p + 1.0) / (t + 1.0) - ( p * 1.0)/t

        heap = [(-gain(p,t),p, t) for p,t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g,p,t = heapq.heappop(heap)
            p,t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p,t),p ,t))
        
        total = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += float(p) / t
        return total/ len(classes)
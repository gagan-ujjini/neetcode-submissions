class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for n in nums:
            if n not in frequency:
                frequency[n] = 1
            else:
                frequency[n] += 1

        minHeap = []
        for (num, freq) in frequency.items():   # total we do for m elements
            heapq.heappush(minHeap, (freq, num)) #logk

            while len(minHeap) > k:
                heapq.heappop(minHeap)  #logk
        
        return [num for (freq, num) in minHeap] #O(n) time

# Time Complexity: O(n + m log k) where m is the number of unique elements. In the worst case (m = n), this becomes O(n log k).
#space complxity: O(m + k) Frequency map: O(m) Heap: O(k). Since m(total number of elements in the input array) can be n(number of unique elements) in the worst case, Space: O(n)
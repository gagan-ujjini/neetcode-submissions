class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #pair: [temperature, index]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]: #current temp > temp on TOS then POP
                stackTemp, stackIdx = stack.pop()
                result[stackIdx] = (i - stackIdx)
            stack.append([temperatures[i], i])
        return result

#T: O(n)
#S: O(n)   